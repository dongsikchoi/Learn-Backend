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

import config # From custom config file

'''
Python : v3.11.4
Selenium : 4.14.0
'''
def clipboard_input(captcha_id, user_input):
    pyperclip.copy(user_input) # input을 클립보드로 복사
    #driver.find_element_by_xpath(user_xpath).click() # element focus 설정
    driver.find_element(By.ID,captcha_id).click()
    
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # ctrl + v 전달

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-popup-blocking')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(config.TARGET_SITE)
driver.implicitly_wait(5)

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

link = driver.find_element(By.XPATH, f"{link_which_you_want}").click()
driver.implicitly_wait(5)

li_element = driver.find_element(By.ID, f'{date_which_you_want}').click()
time.sleep(0.5)
reserve_button = driver.find_element(By.ID, f'{reservation_btn_ID}').click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
captcha = input("Recaptcha: ")
captcha_id = "label-for-captcha"

clipboard_input(driver, captcha_id, captcha)
