# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

request_settings = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': "*/*",
    'Accept-Encoding': 'gazip, deflate, br',
    'Accept-Language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
    'Content-Type': 'text/plain',
    'Connection': 'keep-alive',
    # 'Host': 'wreport1.meituan.net',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=request_settings)

bs_info = bs(response.text, 'html.parser')

list_csv = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    list = []
    list.append(tags.find('span', attrs={'class': 'name'}).text)
    for tag in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        list.append(tag.get_text().replace('\n', '').replace(' ', ''))
    list_csv.append(list[0] + '|' + list[2] + '|' + list[4])

movie = pd.DataFrame(data=list_csv[0:10])
movie.to_csv('./movie.csv', encoding='utf-8', index=False, header=False)
