# 使用requests库获取猫眼电影信息
# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
cookies = {}
a = '__mta=220469159.1593148502368.1593148541623.1593148615270.9; uuid_n_v=v1; uuid=FA517ED0B76B11EA9B3075693A212BAF86111DE4D58A479B9C55DFCEF6A4E4AF; _csrf=ebf6ff89afbf5b791a2de53c842d221b5f100406beb141fbc73c5ca2e3e606e6; _lxsdk_cuid=172ef0ce8e7c8-06a45034ef70ec-f7d1d38-16e360-172ef0ce8e7c8; _lxsdk=FA517ED0B76B11EA9B3075693A212BAF86111DE4D58A479B9C55DFCEF6A4E4AF; mojo-uuid=6ebbd31b9ad2b20a9ca98ee8d16f0a4d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593148500,1593446849; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593448182; __mta=220469159.1593148502368.1593148615270.1593448182326.10; _lxsdk_s=17301221c19-913-0cd-d21%7C%7C1'
for line in a.split(';'):  # 按照字符：进行划分读取
    # 其设置为1就会把字符串拆分成2份
    name, value = line.strip().split('=', 1)
    cookies[name] = value  # 为字典cookies添加内容
# print(cookies)


header = {'user-agent': user_agent}
myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl, headers=header, cookies=cookies)

# print(response.text)

print(f'获取信息返回码是: {response.status_code}')

bs_info = bs(response.text, 'html.parser')
movie = []
movies = []

# 整理获取到的类型字符串


def type_text(typestring):
    updated = typestring.strip().split('\n')[-1].strip()
    return updated
# print(type_text('\n类型:\n              剧情／奇幻\n            '))


# 使用bs4获取电影信息
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    for dtags in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
        for stag in dtags.find_all('span', attrs={'class': 'hover-tag'}):
            if stag.text == '类型:':
                movie_type = type_text(stag.find_parent('div').text)
                # print(movie_type)
            if stag.text == '上映时间:':
                movie_showtime = type_text(stag.find_parent('div').text)
                movie_title = stag.find_parent('div').get('title')
                # print(movie_title)
                movie = [movie_title, movie_type, movie_showtime]
                movies.append(movie)
# print(movies)
# 获取前10条记录用Pandas保存为csv文件
movies_df = pd.DataFrame(movies[0:10], columns=[
                         'Movie_title', 'Movie_type', 'Movie_showtime'])
movies_df.to_csv('./MaoyanTop10MoviesInfo.csv', index=False, encoding='UTF-8')
print('信息保存成功')
