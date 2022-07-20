from selenium.webdriver.common.by import By


class Button():
    def __init__(self, driver):
        self.holder = driver.find_element(By.CLASS_NAME, 'lRwqcd')        
        self.button_field = self.holder.find_element(By.CLASS_NAME, 'uArJ5e')
        
    def click(self):
        self.button_field.click()
        