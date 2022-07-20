from selenium.webdriver.common.by import By
import time
import numpy as np

from iquestion import IQuestion
        

class Text(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.check_type()
        self.answer_field = self.holder.find_element(By.CLASS_NAME, self.row_type)
        
    def check_type(self):
        row_types = ['whsOnd', 'KHxj8b']
        for row_type in row_types:
            rows = self.holder.find_elements(By.CLASS_NAME, row_type)
            if len(rows)>0:
                self.row_type = row_type
                break
        
            
    def answer(self, answer):
        self.answer_field.send_keys(answer)
          
        
class MultipleChoice(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'oyXaNc')
        self.answer_options = self.answer_field.find_elements(By.CLASS_NAME, 'nWQGrd')
        self.answers = list(map(lambda x: x.find_element(By.CLASS_NAME, 'aDTYNe').text, self.answer_options))
        self.check_last_option()
        
    def check_last_option(self):
        #check if the last option is the user's own answer
        try:
            text_holder = self.answer_options[-1].find_element(By.CLASS_NAME, 'pIDwKe')
            self.text_field = text_holder.find_element(By.CLASS_NAME, 'Hvn9fb')
            self.own_answer = True
        except:
            self.own_answer = False
 
    def answer(self, n, text=''):
        ans = self.answer_options[n]
        ans.click()
        if ans == self.answer_options[-1] and self.own_answer:
            self.text_field.send_keys(text)            


class CheckBoxes(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'Y6Myld')
        self.answer_options = self.answer_field.find_elements(By.CLASS_NAME, 'eBFwI')
        self.answers = list(map(lambda x: x.find_element(By.CLASS_NAME, 'aDTYNe').text, self.answer_options))
        self.check_last_option()
        
    def check_last_option(self):
        #check if the last option is the user's own answer
        try:
            text_holder = self.answer_options[-1].find_element(By.CLASS_NAME, 'xVfcde')
            self.text_field = text_holder.find_element(By.CLASS_NAME, 'Hvn9fb')
            self.own_answer = True
        except:
            self.own_answer = False
 
    def answer(self, n, text=''):
        ans = self.answer_options[n]
        ans.click()
        if ans == self.answer_options[-1] and self.own_answer:
            self.text_field.send_keys(text)      


class DropDown(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'vQES8d')
        self.hidden_answers = self.answer_field.find_element(By.CLASS_NAME, 'ry3kXd')
        self.expanded_answers = self.answer_field.find_element(By.CLASS_NAME, 'OA0qNb')

    def answer(self, n):
        self.hidden_answers.click()
        time.sleep(0.3)
        self.answer_options = self.expanded_answers.find_elements(By.CLASS_NAME, 'MocG8c')
        self.answers = list(map(lambda x: x.find_element(By.CLASS_NAME, 'vRMGwf').text,
                                self.answer_options))
        self.answer_options[n].click()


class LinearScale(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'PY6Xd')
        self.answer_holders = self.answer_field.find_elements(By.CLASS_NAME, 'T5pZmf')
        self.answer_options = list(map(lambda x: x.find_element(By.CLASS_NAME, 'eRqjfd'),
                                       self.answer_holders))
        self.answers = list(map(lambda x: x.find_element(By.CLASS_NAME, 'Zki2Ve').text,
                                       self.answer_holders))
        
    def answer(self, n):
        ans = self.answer_options[n]
        ans.click()
        
                    
class Grid(IQuestion):
    ''' Handle Multiple choice grid and Tick box grid questions'''
    def __init__(self, question_holder, row_type=None):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'gTGYUd')
        self.row_type = row_type
        
        if self.row_type is None:
            row_types = ['EzyPc', 'lLfZXe']
            for t in row_types:
                rows = self.answer_field.find_elements(By.CLASS_NAME, t)
                if len(rows)>0:
                    self.row_type = t
                    break
        
        self.grid = self.get_grid()
        self.column_labels = list(map(lambda x: x.text, self.grid[0,1:]))
        self.row_labels = list(map(lambda x: x.text, self.grid[1:,0]))
        self.answer_options = self.grid[1:,1:]

    def get_grid(self):
        grid = []
        row_zero = self.answer_field.find_element(By.CLASS_NAME, 'ssX1Bd')
        rows = self.answer_field.find_elements(By.CLASS_NAME, self.row_type)
        grid.append(row_zero.find_elements(By.CLASS_NAME, 'V4d7Ke'))
        for r in rows:
            grid.append(r.find_elements(By.CLASS_NAME, 'V4d7Ke'))
        return np.array(grid)
           
    def answer(self, *args):
        print(self.column_labels, self.row_labels)
        print(self.grid.shape)
        for arg in args:
            x,y = arg
            self.answer_options[y,x].click()


class Date(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'A6uyJd')
        self.answer_labels = self.set_answer_labels()
        self.date_answer_options = self.answer_field.find_elements(By.CLASS_NAME, 'whsOnd')
       
    def set_answer_labels(self):
        full_date = self.answer_field.find_elements(By.CLASS_NAME, 'ds3H7c')
        date_time = self.answer_field.find_elements(By.CLASS_NAME, 'UaWVmb')
        full_date_label = list(map(lambda x: x.text, full_date))
        date_time_labels = list(map(lambda x: x.text, date_time))
                
        return full_date_label + date_time_labels

        
    def answer(self, args):
        for option in self.date_answer_options:
            option.send_keys(args)
            
            
class Time(IQuestion):
    def __init__(self, question_holder):
        super().__init__(question_holder)
        self.answer_field = self.holder.find_element(By.CLASS_NAME, 'ocBCTb')
        self.answer_labels = self.set_answer_labels()
        self.date_answer_options = self.answer_field.find_elements(By.CLASS_NAME, 'whsOnd')
    
    def set_answer_labels(self):
        full_date = self.answer_field.find_elements(By.CLASS_NAME, 'ds3H7c')
        date_time = self.answer_field.find_elements(By.CLASS_NAME, 'UaWVmb')
        full_date_label = list(map(lambda x: x.text, full_date))
        date_time_labels = list(map(lambda x: x.text, date_time))
        
        return full_date_label + date_time_labels

        
    def answer(self, args):
        for option in self.date_answer_options:
            option.send_keys(args)
        
        

