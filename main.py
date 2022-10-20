import datetime

#главный массив, в котором находятся дни
week = []
day = []

k = False

date_beginning = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().isoweekday() % 7)

date_last = datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.today().isoweekday() % 7)

date = str(date_last.date())

event = dict()
ev = False
file = 'calendar.ics'

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
        if date != str(date_now.date()):
            date = str(date_now.date())
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