from selenium.webdriver.common.by import By

import question
from isection import ISection


def section_handler(driver):
    try:
        section = NextSection(driver)
    except:
        try:
            section = FirstSection(driver)
        except:
            section = SubmittedSection(driver)
    section.set_questions()
    return section
            
class NextSection(ISection):
    def __init__(self, driver):
        super().__init__(driver)
        self.id = self.windows[0].find_element(By.CLASS_NAME, 'aG9Vid').text
        self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        
        
class FirstSection(ISection):
    def __init__(self, driver):
        super().__init__(driver)
        self.id = 'Section 1'
        self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')   
        
        
class SubmittedSection(ISection):
    def __init__(self, driver):
        super().__init__(driver)
        self.id = 'Form Submitted'
        self.button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        
    def answer_questions(self, answers=None):
        self.proceed()
        
# class Section():
#     def __init__(self, driver):
#         self.driver = driver
#         self.form_windows = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
#         self.set_section_id()
#         self.questions = self.clasify_windows()
        
#     def __str__(self):
#         return self.id

    
#     def set_section_id(self):
#         if len(self.form_windows):
#             section_window = self.form_windows[0]
#             try:
#                 sec_id = section_window.find_element(By.CLASS_NAME, 'aG9Vid').text
#                 self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
#                 self.id = sec_id
#             except:
#                 self.button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
#                 self.id = 'Section 1'
#         else:
#             self.button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
#             self.id = 'Submitted'


#     def check_component(self, xpath, organizer):
#         field = self.driver.find_elements(By.XPATH, xpath)
#         if len(field):
#             field_class = field[0].get_dom_attribute('class')
#             component = organizer.get(field_class)
#             return component
        
        
#     def check_question_window(self, index, window, organizer):
#         xpaths = [f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[2]',
#                   f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[3]']
        
#         for xpath in xpaths:
#             q = self.check_component(xpath, organizer)
#             if q is not None:
#                 return q(window)
#         return None
        
    
#     def clasify_windows(self):
#         question_windows = []
#         to_answer = {'AgroKb': question.Text,
#                      'oyXaNc': question.MultipleChoice,
#                      'Y6Myld': question.CheckBoxes,
#                      'vQES8d': question.DropDown,
#                      'PY6Xd':  question.LinearScale,
#                      'e12QUd': question.Grid,
#                      'PfQ8Lb': question.Time}
       
#         for index, window in enumerate(self.form_windows):
#             question_window = self.check_question_window(index, window, to_answer)
#             if question_window is not None:
#                 question_windows.append(question_window)
#             else:
#                 print('Unsupported window type')
#         return question_windows
    
    
#     def get_questions(self):
#         return self.questions
    
#     def proceed(self):
#         # self.buttons.click('Dalej')
#         self.button.click()

    
#     def answer_questions(self, answers):
#         for q in self.questions:
#             question_text = str(q)
#             q.answer(answers.get(question_text))