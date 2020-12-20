import requests
from bs4 import BeautifulSoup

url = 'https://www.lottecinema.co.kr/NLCMW/Cinema/Detail?divisionCode=1&detailDivisionCode=0001&cinemaID=1008'
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.movie_wrap.area_tit')
for i in title_list:
    print(i.select_one('strong'))
