import requests
from datetime import datetime as dt
from bs4 import BeautifulSoup as BS

def masupdate(f, jj):
    for j in jj:
        strin = j.string
        f.append(strin)

hourNow = int(dt.strftime(dt.now(), '%H'))
minuteNow = int(dt.strftime(dt.now(), '%M'))
time = dict(h=hourNow, m=minuteNow)
time['full'] = f'{time['h']}:{time['m']}'
print(time['full'])

station = {
    'Селятино':18203,
    'Аминьевская':40503,
    'Перово':7902,
    'Чухлинка':56408,
    'Нижегород':56308,
    'Ухтомская':8402,
    'Голутвин':12002,
    'Апрелевка':17903
}

start = station.get(input('Откуда:'))
end = station.get(input('Куда:'))
url = 'http://www.tutu.ru/spb/rasp.php?st1={0}&st2={1}&date=today'.format(start, end)
page = requests.get(url)
soup = BS(page.text, "html.parser")

lines = []
lines2 = []

train = soup.findAll('a', class_='g-link desktop__depTimeLink__1NA_N')
pribil = soup.findAll('a', class_='g-link desktop__arrTimeLink__2TJxM')

masupdate(lines, train)
masupdate(lines2, pribil)

fr = dict(zip(lines, lines2))

for k, v in fr.items():
    hours, minutes = map(int, k.split(':'))
    if hours <= time['h'] and minutes <= time['m']:
        print('{0} время прибытия {1}>>>>'.format(k, v))
    elif hours == time['h'] and minutes >= time['m']:
        print('{0} время прибытия {1}'.format(k, v))
    elif hours <= time['h'] and minutes >= time['m']:
        print('{0} время прибытия {1}>>>>'.format(k, v))
    else:
        print('{0} время прибытия {1}'.format(k, v))
