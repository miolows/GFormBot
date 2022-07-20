from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from question import *

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://forms.gle/MkX1C5WE4R3qSh6F6')
set_q = SetQuestions(driver)
questions = set_q.get_questions()


# question_holders = driver.find_elements(By.CLASS_NAME, 'Qr7Oae')
# field = []
# for idx, qh in enumerate(question_holders):
#     question_text_holder = driver.find_element(By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{idx+1}]/div/div/div[1]')
#     question_field_holder = driver.find_element(By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{idx+1}]/div/div/div[2]')

#     question_text = question_text_holder.find_element(By.CLASS_NAME, 'M7eMe').text
#     question_field_class = question_field_holder.get_dom_attribute('class')
#     # field.append(question_field_holder)
#     print(question_text, question_field_class)

# <div jscontroller="oCiKKc" jsaction="rcuQ6b:vZc4S;O22p3e:zjh6rb;b2trFe:eVidQc;sPvj8e:d3sQLd;AHmuwe:h06R8;" class="AgroKb"><div class="rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd" jscontroller="pxq3x" jsaction="clickonly:KjsqPd; focus:Jt1EX; blur:fpfTEe; input:Lg5SV" jsshadow="" jsname="YPqjbf"><div class="aCsJod oJeWuf"><div class="aXBtI Wic03c"><div class="Xb9hP"><input type="text" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="off" tabindex="0" aria-labelledby="i1" aria-describedby="i2 i3" dir="auto" data-initial-dir="auto" data-initial-value=""><div jsname="LwH6nd" class="ndJi5d snByac" aria-hidden="true">Twoja odpowiedź</div></div><div class="i9lrp mIZh1c"></div><div jsname="XmnwAc" class="OabDMe cXrdqd"></div></div></div><div class="LXRPh"><div jsname="ty6ygf" class="ovnfwe Is7Fhb"></div></div></div></div>
for q in questions:
    try:
        q.answer(1)
    except:
        q.answer((1,1))

# questions[9].answer(1)

# button = Button(driver)
# button.click()
