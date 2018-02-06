#!/usr/bin/env python3

import csv

from bs4 import BeautifulSoup
import requests

with open('fred_frontpage.csv', 'w') as f:
    soup = BeautifulSoup(requests.get('https://fred.stlouisfed.org').text, 'html')
    writer = csv.writer(f)
    for link in soup.find_all('a'):
        writer.writerow([link.get('href')])
print('I\'m done')
