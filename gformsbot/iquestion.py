from selenium.webdriver.common.by import By


class IQuestion():
    def __init__(self, question_holder):
        self.holder = question_holder
        
        self.question = self.holder.find_element(By.CLASS_NAME, 'M7eMe').text
        self.required = self.is_required()
        print(self.question)

    def is_required(self):
        req = self.holder.find_elements(By.CLASS_NAME, 'vnumgf')
        if len(req)>0:
            return True
        else:
            return False