from selenium.webdriver.common.by import By


class IQuestion():
    def __init__(self, question_window, *args):
        self.window = question_window
        self.required = self.is_required(question_window)
        self.question_text = self.element_text(question_window, 'M7eMe')
        self.answer_field = self.set_answer_field(question_window, *args)

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
        if len(req)>0:
            return True
        else:
            return False
    
    def is_required(self, holder):
        return self.contains(holder, 'vnumgf')
    
    def set_answer_field(self, holder, *args):
        for c in args:
            out = self.elements(self.window, c)
            if len(out)>0:
                return out[0]
                break    

                
class IChoiceQuestion(IQuestion):
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
 
    
    def answer(self, n, text=''):
        ans = self.answer_options[n]
        ans.click()
        
        if ans == self.answer_options[-1]:
            if self.own_answer is not None:
                self.own_answer.send_keys(text)   