import datetime
import os

#главный массивы, в которых формируется расписание на каждый день и на неделю
week = []
day = []

k = False

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
file = finder('RUZ_17.10.2022-23.10.2022_314.ics','C:/')

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