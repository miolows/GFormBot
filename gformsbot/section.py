from selenium.webdriver.common.by import By

import question
import ignore
from button import Button

class Section():
    def __init__(self, driver):
        self.driver = driver
        self.form_windows = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
        self.id = self.set_section_id()
        self.questions = self.clasify_windows()
        self.buttons = Button(driver)
        print(self.id)

    
    def set_section_id(self):
        if len(self.form_windows):
            section_window = self.form_windows[0]
            try:
                sec_id = section_window.find_element(By.CLASS_NAME, 'aG9Vid').text
                self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
                return sec_id
            except:
                self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
                return 'Section 1'
        else:
            self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
            return 'Submitted'

    def check_component(self, xpath, organizer):
        field = self.driver.find_elements(By.XPATH, xpath)
        if len(field):
            field_class = field[0].get_dom_attribute('class')
            component = organizer.get(field_class)
            return component
        
        
    def check_question_window(self, index, window, organizer):
        xpaths = [f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[2]',
                  f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[3]']
        
        for xpath in xpaths:
            q = self.check_component(xpath, organizer)
            if q is not None:
                return q(window)
        return None
        
    
    def clasify_windows(self):
        question_windows = []
        to_answer = {'AgroKb': question.Text,
                     'oyXaNc': question.MultipleChoice,
                     'Y6Myld': question.CheckBoxes,
                     'vQES8d': question.DropDown,
                     'PY6Xd':  question.LinearScale,
                     'e12QUd': question.Grid,
                     'PfQ8Lb': question.Time}
       
        for index, window in enumerate(self.form_windows):
            question_window = self.check_question_window(index, window, to_answer)
            if question_window is not None:
                question_windows.append(question_window)
            else:
                print('Unsupported window type')
        return question_windows
    
    
    def get_questions(self):
        return self.questions
    
    def proceed(self):
        # self.buttons.click('Dalej')
        self.button.click()

    
    def answer_questions(self, answers):
        for q in self.questions:
            question_text = str(q)
            q.answer(answers.get(question_text))    
    
            
        #     question_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[2]'
        #     q = self.check_component(question_xpath, to_answer)
        #     if q is None:
        #         question_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[3]'                
        #         q = self.check_component(question_xpath, to_answer)
        #         if q is None:
        #             print('Unsupported window type')
        #         else:
        #             question_windows.append(q(window))
        #     else:
        #         question_windows.append(q(window))
    
        # return question_windows
            
        
        
        
    # def check_component(self, xpath, organizer):
    #     field = self.driver.find_elements(By.XPATH, xpath)
    #     if len(field):
    #         return
    #     else:
    #         field_class = field[0].get_dom_attribute('class')
    #         component = organizer.get(field_class)
    #         print(component)
    #         return component


    # def clasify_windows(self):
    #     to_ignore = {'gCouxf': ignore.Image,
    #                  'KkG9vf': ignore.SectionInfo,
    #                  'OxAavc': ignore.Media}
        
    #     to_answer = {'AgroKb': question.Text,
    #                  'oyXaNc': question.MultipleChoice,
    #                  'Y6Myld': question.CheckBoxes,
    #                  'vQES8d': question.DropDown,
    #                  'PY6Xd':  question.LinearScale,
    #                  'e12QUd': question.Grid,
    #                  'PfQ8Lb': question.Time}
        
    #     form_windows = self.driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
        
    #     ignored_windows = []
    #     question_windows = []

    #     for index, window in enumerate(form_windows):
    #         ignore_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div'
    #         i = self.check_component(ignore_xpath, to_ignore)
    #         if i is None:
    #             question_xpath = f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[2]'
    #             q = self.check_component(question_xpath, to_answer)
    #             if q is None:
    #                 print("Unsupported question type")
    #             else:
    #                 question_windows.append(q(window))
    #         else:
    #             ignored_windows.append(i(window))

    #     return ignored_windows, question_windows
    

