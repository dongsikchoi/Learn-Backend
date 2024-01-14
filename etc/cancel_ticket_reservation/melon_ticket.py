import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip 
from selenium.webdriver.support.ui import WebDriverWait, Select

import random
import config # From custom config file

'''
Python : v3.11.4
Selenium : 4.14.0
'''
def clipboard_input(driver,captcha_id, user_input):
    pyperclip.copy(user_input) # input을 클립보드로 복사
    driver.find_element(By.CSS_SELECTOR,captcha_id).click()
    
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # ctrl + v 전달
    time.sleep(1)
    

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-popup-blocking')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(config.TARGET_SITE)
driver.implicitly_wait(5)
print(driver.page_source)


login_button = driver.find_element(By.CSS_SELECTOR,'a.btn_g_login')
login_button.click()
driver.implicitly_wait(5)

login_button = driver.find_element(By.XPATH,"//button[@title='카카오계정 로그인']")
login_button.click()


driver.implicitly_wait(5)
time.sleep(1)


driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(5)

username_input = driver.find_element(By.ID,'loginId--1')
username_input.clear()  
username_input.send_keys(config.USER_INFO['ID'])

password_input = driver.find_element(By.ID,'password--2')
password_input.clear() 
password_input.send_keys(config.USER_INFO['PW'])
login_button = driver.find_element(By.XPATH,'//button[contains(text(), "로그인")]').click()

time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.implicitly_wait(5)

search_input = driver.find_element(By.ID, 'top_search')
search_input.clear() 
search_input.send_keys(config.search_keyword)

search_btn = driver.find_element(By.ID, 'btn_top_search').click()
driver.implicitly_wait(5)

# 대상 공연 링크
link = driver.find_element(By.XPATH, config.TARGET_CONCERT_LINK).click()

driver.implicitly_wait(5)


# #날짜 선택 있으면 추가 

notic_checkbox = driver.find_element(By.ID,'noticeAlert_layerpopup_cookie').click() # << 01.14 추가 [추가 티켓오픈에 따른 예매 매수 제한 변경 안내] 뜨면 이거 추가해주면 됨

time.sleep(0.5)
reserve_button = driver.find_element(By.ID, 'ticketReservation_Btn').click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
captcha = input("Recaptcha: ")
captcha_id = 'label[for="label-for-captcha"]'
clipboard_input(driver, captcha_id, captcha)
driver.find_element(By.ID,"btnComplete").click()
time.sleep(1)
wait = WebDriverWait(driver, 5)  

iframe_element = driver.find_element(By.ID,'oneStopFrame')
driver.switch_to.frame(iframe_element)
inner_html_element = driver.find_element(By.TAG_NAME,'html')
inner_html_text =inner_html_element.text

# 좌석 등급 
tr_element = driver.find_element(By.ID,"gd10009").click()  
time.sleep(3)

while True:
    wait = WebDriverWait(driver, 1)  
    div = driver.find_elements(By.XPATH, "//div[@class='list_area listOn']")
    print(f'div = {div}')
    li_tags = div[0].find_elements(By.TAG_NAME,"li")
    print(f'li_tags = {li_tags}')
    is_zero = False
    for li in li_tags:
        residual = li.find_element(By.CLASS_NAME,'seat_residual')
        res = residual.find_element(By.TAG_NAME,'strong').text
        print(res)
        if res != '0':
            is_zero = True 
            li.click()
            break
    if is_zero:
        break
    else:
        refresh_link = driver.find_element(By.ID, "btnReloadSchedule")
        refresh_link.click()
        time.sleep(random.uniform(1,3) )

print(f'나왔다!')
canvas = driver.find_element(By.ID,'ez_canvas')
grapes = canvas.find_elements(By.TAG_NAME,'rect')

is_success = False 
for grape in grapes:
    try:
        value = grape.get_attribute("fill")
        if value != '#DDDDDD':
            grape.click() 

            next_button = driver.find_element(By.ID,"nextTicketSelection").click()
            is_success=True
            break
    except:
        continue
if is_success:
    driver.execute_script("alert('알람 테스트');")
