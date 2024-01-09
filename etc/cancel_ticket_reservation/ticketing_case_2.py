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

# 대상 공연 링크 - 링크 들어가면 /performance/index.htm?prodId={number} 나오는데 이 부분 아래에 넣어주면 됨
link = driver.find_element(By.XPATH, "//a[contains(@href,'/performance/index.htm?prodId={num}')]").click() 

driver.implicitly_wait(5)

#날짜
'''
날짜를 선택하고 시간까지 선택하는 케이스
'''
next_month = driver.find_element(By.CLASS_NAME,'btn_calendar_next').click()
WebDriverWait(driver,1)  
li_element = driver.find_element(By.ID, 'calendar_SelectId_20231231').click() 
WebDriverWait(driver,1) 
time.sleep(1)

time_select= driver.find_element(By.CSS_SELECTOR,'p.casting-name').click()
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
time.sleep(3)

is_complete = False

while True:
    #wait = WebDriverWait(driver, 1)  
    canvas = driver.find_element(By.ID,'ez_canvas')
    grapes = canvas.find_elements(By.TAG_NAME,'rect')
    count = 0
    '''
    이렇게 좌석 등급 선택 없이 바로 좌석 선택으로 들어가는 예매의 경우 좌석이 너무 많아서 오래 걸림. (내가 시도한 예매는 1300석)
    
    중앙에 앞자리 좌석이 타겟이라 x, y 좌표값 범위 지정
    
    index = 0
    for grape in grapes:
        x = float(grape.get_attribute('x'))
        y = float(grape.get_attribute('y'))
        fill = grape.get_attribute('fill')
        if (217.22 <= x <= 425.22) and (109.11 <= y <= 161.11) and (fill != '#DDDDDD'): 
            index_list.append(index)
        index += 1 
    
    이런 식으로 인덱스 먼저 구하고 그 인덱스로 반복문 돌리는 편이 빠름 
    '''
    index_list = [557, 558, 560, 566, 567, 568, 569, 574, 576, 578, 583, 585, 586, 587, 588, 593, 
                  595, 597, 601, 603, 604, 606, 607, 612, 620, 621, 622, 624, 625, 629, 631, 634, 
                  635, 636, 637, 638, 639, 644, 646, 651, 656, 657, 658, 664, 666, 669, 670, 674, 
                  680, 681, 683, 686, 690, 692, 693, 694, 697, 698, 699, 707, 708, 709, 710, 711, 
                  715, 718, 723, 724, 725, 726, 727, 734, 737, 740, 743, 744, 746, 747, 753, 754, 
                  773, 776, 777, 778, 779, 785, 787, 791, 793, 794, 795, 796, 803, 804, 809, 811, 
                  812, 813, 814, 819, 820, 824, 827, 831, 835, 838, 839, 846, 848, 849, 850, 851, 
                  852, 853, 854, 860, 862, 863, 865, 866, 872, 873, 880, 883, 884, 885, 890, 
                  891, 905, 906, 910, 911]
    
    for index in index_list:
        grape = grapes[index]
        x = float(grape.get_attribute('x'))
        y = float(grape.get_attribute('y'))
        fill = grape.get_attribute('fill')
        if fill != '#DDDDDD':
            is_complete=True
            grape.click()
            next_button = driver.find_element(By.ID,"nextTicketSelection").click()
            break 

    if is_complete:
        break
    refresh_link = driver.find_element(By.ID, "btnReloadSchedule")
    refresh_link.click()
    time.sleep(random.uniform(0.5,1) )

if is_complete:
    print(f'나왔다!')
    for _ in range(100):
        print('*'*10)

    



