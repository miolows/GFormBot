from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from gformsbot.set import SetQuestions

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://forms.gle/MkX1C5WE4R3qSh6F6')

set_q = SetQuestions(driver)
questions = set_q.get_questions()

for q in questions:
    print(q)
    try:
        q.answer(1)
    except:
        q.answer((1,1))


# button = Button(driver)
# button.click()
