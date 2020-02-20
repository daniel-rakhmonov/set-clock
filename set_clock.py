#!/usr/bin/python3

# daniel-rakhmonov

from bs4 import BeautifulSoup
from os import system
import urllib.request

url = 'http://worldtimeapi.org'

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
list_item = soup.find('div', attrs={'class': 'result'})
name = list_item.text.strip()
name2 = name.split()[16]

mo = name2[5:7]
da = name2[8:10]
hr = name2[11:13]
mi = name2[14:16]
ye = name2[0:4]
se = name2[17:19]

exec1 = system('date %s%s%s%s%s.%s' % (mo,da,hr,mi,ye,se))


