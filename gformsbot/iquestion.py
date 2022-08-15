from selenium.webdriver.common.by import By
import functools
import time

class SkipError(Exception):
    pass

class AnswerError(Exception):
    pass

class IQuestion():
    def __init__(self, question_window, *args):
        self.window = question_window
        self.required = self.is_required(question_window)
        self.error_field = self.element(question_window, 'SL4Sz')
        self.question_text = self.element_text(question_window, 'M7eMe')
        self.answer_field = self.find_field(question_window, *args)

    def __str__(self):
        return self.question_text
    
    def element(self, holder, class_name):
        return holder.find_element(By.CLASS_NAME, class_name)
    
    def element_text(self, holder, class_name):
        return self.element(holder, class_name).text
    
    def elements(self, holder, class_name):
        return holder.find_elements(By.CLASS_NAME, class_name)    
    
    def elements_text(self, elements_list):
        return [element.text for element in elements_list]
    
    def all_elements(self, holders_list, class_name):
        return [self.element(holder, class_name) for holder in holders_list]
    
    def all_elements_text(self, holders_list, class_name):
        return [self.element(holder, class_name).text for holder in holders_list]
    
    def contains(self, holder, class_name):
        req = self.elements(holder, class_name)
        return bool(len(req))
    
    def is_required(self, holder):
        return self.contains(holder, 'vnumgf')
    
    def find_field(self, holder, *args):
        for c in args:
            out = self.elements(self.window, c)
            if len(out):
                return out[0]
                break
            
    def answer_dict(self, labels, options):
        ans_dict = {labels[i]: options[i] for i in range(len(labels))}
        return ans_dict
    
    def skip(self):
        if self.required:
            raise SkipError(f'Question "{self}" is required and cannot be skipped.')
        else:
            pass


class IMultiChoiceQuestion(IQuestion):
    def __init__(self, question_holder, options_class, **kwargs):
        super().__init__(question_holder, options_class)
        self.answer_options = self.elements(self.answer_field, kwargs['options'])
        self.answer_labels = self.all_elements_text(self.answer_options, kwargs['labels'])
        self.own_answer = self.last_option(kwargs['text_holder'], kwargs['text'])

        
    def last_option(self, text_holder_class, text_class):
        #check if the last option is the user's own answer
        lst_option = self.answer_options[-1]
        if self.contains(lst_option, text_holder_class):
            text_holder = self.element(lst_option, text_holder_class)
            text = self.element(text_holder, text_class)
            return text
        else:
            return None
 
    # @error_check
    def answer(self, *answers):
        answers_d = self.answer_dict(self.answer_labels, self.answer_options)
        for ans in answers:
            a = answers_d.get(ans)
            if a is not None:
                a.click()
            else:
                if self.own_answer is not None:
                    self.own_answer.send_keys(ans)