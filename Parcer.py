import requests
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
regURL = 'https://portal.unn.ru/auth/?backurl=%2Fstream%2F'
timetableURL = 'https://portal.unn.ru/ruz/main?login=yes&_url=%2Fmain'




url = 'https://portal.unn.ru/auth/?backurl=%2Fstream%2F'


USER_LOGIN = 's22380095'
USER_PASSWORD = 'etomyvuz2004'
group = '3822Б1ПМ1'
FIO = 'Зазнобин Петр Викторович'


user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'




#Вход на сайт по рабоче-крестьянски
options = Options()
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://portal.unn.ru/ruz/main')
driver.find_element("name", "USER_LOGIN").send_keys(USER_LOGIN)
driver.find_element("name", "USER_PASSWORD").send_keys(USER_PASSWORD)
loginbtn = driver.find_element(By.CLASS_NAME,"login-btn")
loginbtn.click()
driver.switch_to.window(driver.window_handles[-1])
current = driver.current_url
print(current)


#Нажатие на кнопку скачивания
driver.get('https://portal.unn.ru/ruz/main')
driver.find_element("name", "group").send_keys(group)
time.sleep(1)
pyautogui.press("Enter")
time.sleep(1)

download = driver.find_element(By.CLASS_NAME,"fa-calendar")
download.click()
time.sleep(60)

#Вход успешно воспроизведен и мы сохраняем страницу в html файл
print(requests.get('https://portal.unn.ru/ruz/main'))
driver.quit()