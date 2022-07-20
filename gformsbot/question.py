from selenium.webdriver.common.by import By
import time
import numpy as np

from iquestion import IQuestion, IChoiceQuestion
        

class Text(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'whsOnd', 'KHxj8b')
    
    def answer(self, answer):
        self.answer_field.send_keys(answer)
          
        
class MultipleChoice(IChoiceQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'oyXaNc', 
                         options='nWQGrd', labels='aDTYNe', text_holder='pIDwKe', text='Hvn9fb')
        

class CheckBoxes(IChoiceQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'Y6Myld', 
                         options='eBFwI', labels='aDTYNe', text_holder='xVfcde', text='Hvn9fb')
        

class LinearScale(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'N9Qcwe')
        self.answer_options = self.elements(self.answer_field, 'T5pZmf')
        self.answer_labels = self.all_elements_text(self.answer_options, 'Zki2Ve')
        print(self.answer_labels)


    def answer(self, n):
        ans = self.answer_options[n]
        ans.click()
        

class DropDown(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'vQES8d')
        self.hidden_answers = self.element(self.answer_field, 'ry3kXd')
        self.expanded_answers = self.element(self.answer_field, 'OA0qNb')

    def expand(self):
        self.hidden_answers.click()
        time.sleep(0.3)
        self.answer_options = self.elements(self.expanded_answers, 'MocG8c')
        self.answer_labels = self.all_elements_text(self.answer_options, 'vRMGwf')

    def answer(self, n):
        self.expand()
        self.answer_options[n].click()


class Grid(IQuestion):
    ''' Handle Multiple choice grid and Tick box grid questions'''
    def __init__(self, question_window):
        super().__init__(question_window, 'gTGYUd')        
        self.grid = self.get_grid()
        self.column_labels = self.elements_text(self.grid[0,1:])
        self.row_labels = self.elements_text(self.grid[1:,0])
        self.answer_options = self.grid[1:,1:]
        
    def get_rows(self, holder):
        row_types = ['EzyPc', 'lLfZXe']
        for row_type in row_types:
            out = self.elements(holder, row_type)
            if len(out)>0:
                return out
                break    

    def get_grid(self):
        grid = []
        header = self.element(self.answer_field, 'ssX1Bd')
        rows = self.get_rows(self.answer_field)
        header_elements = self.elements(header, 'V4d7Ke')
        
        grid.append(header_elements)
        for row in rows:
            row_elements = self.elements(row, 'V4d7Ke')
            grid.append(row_elements)
            
        return np.array(grid)
           
    
    def answer(self, *args):
        for arg in args:
            x,y = arg
            self.answer_options[y,x].click()


class Date(IQuestion):
    def __init__(self, question_window):
        super().__init__(question_window, 'A6uyJd')
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
    def __init__(self, question_window):
        super().__init__(question_window, 'ocBCTb')
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
        
        

