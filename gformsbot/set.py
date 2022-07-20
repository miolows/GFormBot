from selenium.webdriver.common.by import By

from question import Text, MultipleChoice, CheckBoxes, DropDown, LinearScale, Grid, Time, Date

class SetQuestions():
    def __init__(self, driver):
        self.questions = self.set_question_types(driver)
        
    def set_question_types(self, driver):
        type_classes = {'AgroKb': Text,
                        'oyXaNc': MultipleChoice,
                        'Y6Myld': CheckBoxes,
                        'vQES8d': DropDown,
                        'PY6Xd':  LinearScale,
                        'e12QUd': Grid,
                        'PfQ8Lb': Time,
                        None:     None}
        
        type_jscontroller= {"lLliLe": Date}
        
        q_windows = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
        questions = []
        
        for idx, window in enumerate(q_windows):
            field_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{idx+1}]/div/div/div[2]'
            question_field_holder = driver.find_element(By.XPATH, field_xpath)
            field_class = question_field_holder.get_dom_attribute('class')
            
            if field_class is not None:
                question = type_classes[field_class](window)
                questions.append(question) 
            else:
                field_jscontroller = question_field_holder.get_dom_attribute('jscontroller')
                question = type_jscontroller[field_jscontroller](window)
                questions.append(question)
                
        return questions


    def get_questions(self):
        return self.questions