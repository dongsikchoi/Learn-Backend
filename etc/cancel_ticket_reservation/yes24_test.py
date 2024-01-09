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
chrome_options.add_argument('--ignore-certificate-errors') #Error parsing cert retrieved from AIA (as DER): << 에러 방지
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(config.TARGET_SITE_YES24)
driver.implicitly_wait(5)


username_input = driver.find_element(By.ID,"SMemberID")
username_input.clear()  
username_input.send_keys(config.YES24_INFO['ID'])

password_input = driver.find_element(By.ID,"SMemberPassword")
password_input.clear() 
password_input.send_keys(config.YES24_INFO['PW'])
login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/button/span').click()
driver.get(config.TARGET_SITE_YES24_RESERVATION)

reservation_btn = driver.find_element(By.XPATH,'/html/body/form/div[9]/div/div[4]/a[4]').click()
time.sleep(3)
all_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(5)
time.sleep(3)
date_select = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[7]/a").click()
time.sleep(1)
next_step = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div/img").click()
