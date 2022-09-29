from urllib import request
import requests
from bs4 import BeautifulSoup
# from html_table_parser import parser_functions

url = 'https://genshin-impact.fandom.com/wiki/Promotional_Code'

request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')
data = soup.find('table', {'class': 'wikitable'})
print(data)
