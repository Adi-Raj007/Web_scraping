import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage = requests.get("https://www.wikirating.com/list-of-corporations-by-credit-rating/", headers=headers).text

soup = BeautifulSoup(webpage, 'lxml')

def print_rows_and_columns(soup):
    for i in range(0, 148):
        print(soup.find_all('tr')[i].text)

print_rows_and_columns(soup)

data = []
for i in range(1, 148):
    row = soup.find_all('tr')[i].text.strip().split('\n')
    data.append(row)

df = pd.DataFrame(data, columns=['ID', 'Logo', 'Corporate', 'Headquarter', 'CAI', 'CAI update', 'not used', 'S&P', "Moody's", 'Fitch', 'Last update'])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)
print(df)

df.to_csv('credit_ratings.csv', index=False)
