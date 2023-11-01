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
from selenium.webdriver.support.ui import WebDriverWait
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

driver.find_element(By.ID,"btnComplete").click()
time.sleep(1)
wait = WebDriverWait(driver, 5)  

iframe_element = driver.find_element(By.ID,f'{iframe_id}') # iframe 내에 html 소스가 있음
driver.switch_to.frame(iframe_element)

inner_html_element = driver.find_element(By.TAG_NAME,'html')
inner_html_text =inner_html_element.text

tr_element = driver.find_element(By.ID,f"{seat_grade_id}").click()
time.sleep(3)

while True:
    wait = WebDriverWait(driver, 1)  
    div = driver.find_elements(By.XPATH, f"{parent_div}']")
    li_tags = div[0].find_elements(By.TAG_NAME,"li")
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
    refresh_link = driver.find_element(By.ID, f"{refresh_link}")
    refresh_link.click()
    time.sleep(random.uniform(1,3) )

print(f'나왔다!')
canvas = driver.find_element(By.ID,f'{grape_canvas}')
grapes = canvas.find_elements(By.TAG_NAME,'rect')

is_success = False 
for grape in grapes:
    try:
        value = grape.get_attribute("fill")
        if value != 'f{blank_color}':
            grape.click() 

            next_button = driver.find_element(By.ID,"nextTicketSelection").click()
            is_success=True
            break
    except:
        continue
if is_success:
    driver.execute_script("alert('완료');")

