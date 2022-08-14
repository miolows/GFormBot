from selenium.webdriver.common.by import By
from abc import ABC, abstractmethod

import question
import ignore

class ISection():
    def __init__(self, driver):
        self.driver = driver
        self.windows = self.driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
        
    def __str__(self):
        return self.id
    
    def set_questions(self):
        self.questions = self.clasify_windows(self.windows)
    
    def check_component(self, xpath, organizer):
        field = self.driver.find_elements(By.XPATH, xpath)
        if len(field):
            field_class = field[0].get_dom_attribute('class')
            component = organizer.get(field_class)
            return component
        
    def find_error(self):
        error_msg = []
        for w in self.questions:
            error = [e.text for e in w.error_field.find_elements(By.CLASS_NAME, 'RHiWt')]
            print(len(error))
            if len(error):
                error_msg.append([str(w), error[0]])
        return error_msg
        
    def check_question_window(self, index, window, organizer):
        xpaths = [f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[2]',
                  f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{index+1}]/div/div/div[3]']
        
        for xpath in xpaths:
            q = self.check_component(xpath, organizer)
            if q is not None:
                return q(window)
        return None
    
    
    def clasify_windows(self, windows):
        question_windows = []
        to_answer = {'AgroKb': question.Text,
                     'oyXaNc': question.MultipleChoice,
                     'Y6Myld': question.CheckBoxes,
                     'vQES8d': question.DropDown,
                     'PY6Xd':  question.LinearScale,
                     'e12QUd': question.Grid,
                     'PfQ8Lb': question.Time}
       
        for index, window in enumerate(windows):
            question_window = self.check_question_window(index, window, to_answer)
            if question_window is not None:
                question_windows.append(question_window)
            # else:
            #     print('Unsupported window type')
        return question_windows
    
    
    def proceed(self):
        self.button.click()

    
    def answer_questions(self, answers=None):
        if answers is not None:
            for q in self.questions:
                question_text = str(q)
                q.answer(*answers.get(question_text))
        else:
            for q in self.questions:
                q.skip()
    