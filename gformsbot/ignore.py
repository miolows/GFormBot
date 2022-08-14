from selenium.webdriver.common.by import By

class IIgnore():
    def __init__(self, question_window, window_type):
        self.window = question_window
        self.holder = question_window.find_element(By.CLASS_NAME, window_type)
        
    def answer(self, *args, **kwargs):
        pass
        
    
class SectionInfo(IIgnore):
    def __init__(self, question_window):
        super().__init__(question_window, 'KkG9vf')


class Media(IIgnore):
    def __init__(self, question_window):
        super().__init__(question_window, 'OxAavc')


class Image():
    def __init__(self, question_window):
        print("Image")