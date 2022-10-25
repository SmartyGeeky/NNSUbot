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
time.sleep(5)

#Вход успешно воспроизведен и мы сохраняем страницу в html файл
print(requests.get('https://portal.unn.ru/ruz/main'))
driver.quit()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import datetime
import os

#главный массивы, в которых формируется расписание на каждый день и на неделю
week = []
day = []

k = False

first = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().isoweekday() % 7 - 1)
second = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().isoweekday() % 7 - 7)

group = '3822Б1ПМ1'

way = 'RUZ_' + datetime.datetime.strftime(first, '%d.%m.%Y') + '-' + datetime.datetime.strftime(second, '%d.%m.%Y') + '_' + group + '.ics'
#нахождение верного пути к файлу
def finder(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

#для отслеживания начала недели
date_last = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.today().isoweekday() % 7)

#создание элемента в расписании
event = dict()
ev = False
print('new code')
file = finder(way, 'C:/Users/pitza/Downloads/')

print(file)

#функция, создающая ивент в дне
def create(string):
    a = string.split(':')
    if len(a) != 1:
        if a[0] == 'DTSTART' or a[0] == 'DTEND':
            date = a[1][0:4] + '/' + a[1][4:6] + '/' + a[1][6:8] + ' ' + a[1][9:11] + ':' + a[1][11:13] + ':' + a[1][13:15]
            event[a[0]] = date
        else:
            event[a[0]] = a[1]

#открытие файла с расписанием
lines = open(file, encoding = 'utf8').readlines()

#создание расписания
for s in lines:
    if 'DTSTART' in s or 'DTEND' in s or 'SUMMARY' in s or 'LOCATION' in s:
        create(s)
    if 'END:VEVENT' in s:
        date_now = datetime.datetime.strptime(event['DTSTART'], '%Y/%m/%d %H:%M:%S')
        if date_last.date() != date_now.date():
            date_last = date_now
            if k == True:
                week.append(day.copy())
                day.clear()
            else:
                k = True
            day.append(event.copy())
        else:
            day.append(event.copy())
        event.clear()
week.append(day.copy())
#вывод
for i in week:
    print(i)
os.remove(file)