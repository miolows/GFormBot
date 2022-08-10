from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import json
import os
import time

from gformsbot.section import section_handler

class Bot():
    def __init__(self, web_adress, forms_to_fill, answer_dir='./answers'):
        self.driver = self.set_driver()
        self.driver.get(web_adress)
        self.answer_dir = answer_dir
        self.forms = forms_to_fill
        self.index = 0
    
    def set_driver(self):
        driver_path = ChromeDriverManager().install()
        service = ChromeService(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--lang=en")
        # options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    
    def set_section(self):
        section = section_handler(self.driver)
        return section
        
    def load_answer_file(self, file_name):
        path = os.path.join(self.answer_dir, f'{file_name}.json')
        try:
            with open(path, "r") as json_file:      
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            return None
        
        
    def answer_section_question(self, section):
        if section.questions:
            section_answers = self.load_answer_file(str(section))
            section.answer_questions(section_answers)
            
            
    def fill_forms(self):
        while self.index < self.forms:
            section = self.set_section()
            if str(section) == 'Form Submitted':
                self.index = self.index + 1
            else:
                self.answer_section_question(section)
                
            section.proceed()
            time.sleep(0.3)
        self.driver.close()