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
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(config.TARGET_SITE_YES24) # 예스24 메인 페이지 링크 ; https://www[.]yes24[.]com/Templates/FTLogin.aspx
driver.implicitly_wait(5)

username_input = driver.find_element(By.ID,"SMemberID")
username_input.clear()  
username_input.send_keys(config.YES24_INFO['ID'])
password_input = driver.find_element(By.ID,"SMemberPassword")
password_input.clear() 
password_input.send_keys(config.YES24_INFO['PW'])

login_button = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div[2]/form/fieldset/button/span').click()
driver.get(config.TARGET_SITE_YES24_RESERVATION) # 예매하고자 하는 공연 링크 ex; http://ticket[.]yes24[.]com/Perf/12345
time.sleep(3)
time_select = driver.find_element(By.XPATH,'//*[@id="PerfPlayTime"]/a').click()
time.sleep(1)
reservation_btn = driver.find_element(By.XPATH,'//*[@id="mainForm"]/div[10]/div/div[4]/a[4]').click()
time.sleep(1)
all_handles = driver.window_handles
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(5)
time.sleep(3)
date_select = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[7]/a").click()
time.sleep(1)
next_step = driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div/img").click()
wait = WebDriverWait(driver, 5)  
time.sleep(5)

iframe_element = driver.find_element(By.TAG_NAME,'iframe')
driver.switch_to.frame(iframe_element)
inner_html_element = driver.find_element(By.TAG_NAME,'html')
inner_html_text =inner_html_element.text
count = 0
is_success=False


area_list = [] 
for i in range(2):
    tmp_area = 'area' + str(i)
    area_list.append(tmp_area)
count = 0
while True:
    count += 1
    if count % 10 == 0:
        print(f'{count} 회..')
    for area in area_list:
        
        driver.find_element(By.ID,area).click()
        div_tags = driver.find_elements(By.XPATH,"//div[@id='divSeatArray']/div")
        for div_tag in div_tags:
            value = div_tag.get_attribute("class")
            if value != 's13':
                print('='*100)
                div_tag.click()
                is_success=True
                driver.find_element(By.XPATH,'/html/body/form/div[3]/div[2]/div/div[2]/p[2]/a').click()
                driver.execute_script("alert('알람 테스트');")
                break
        time.sleep(random.uniform(0.5,0.7) )
        