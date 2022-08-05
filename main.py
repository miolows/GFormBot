# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromiumService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.utils import ChromeType
# import time

# from gformsbot.section import Section
# import answer

# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

import time

from gformsbot.section import Section
import answer
# prefs = {
#   "translate_whitelists": {"your native language":"en"},
#   "translate":{"enabled":"True"}
# }
# options.add_experimental_option("prefs", prefs)

# options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US,en_GB'})






driver_path = ChromeDriverManager().install()
service = ChromeService(driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--lang=en")
options.add_argument("--html_lang=en")
# options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://forms.gle/MkX1C5WE4R3qSh6F6')

ans = [answer.section_1, answer.section_2, answer.section_3, answer.section_4]

for a in ans:
    time.sleep(0.3)
    section = Section(driver)
    section.answer_questions(a)
    section.proceed()
    




# questions = set_q.get_questions()

# for q in questions:
    
#     print(q)
#     # print(type(answer.answers[str(q)]))
#     q.answer(answer.answers[str(q)])
#     # try:
        
#     # except:
#     #     q.answer((1,1))


# # button = Button(driver)
# # button.click()
