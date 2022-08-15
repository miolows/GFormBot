from selenium.webdriver.common.by import By

import question
from isection import ISection

            
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