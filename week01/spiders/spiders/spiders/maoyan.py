import scrapy
from bs4 import BeautifulSoup
from spiders.items import SpidersItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    # define name of spider
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    cookies = {}
    a = '__mta=220469159.1593148502368.1593148541623.1593148615270.9; uuid_n_v=v1; uuid=FA517ED0B76B11EA9B3075693A212BAF86111DE4D58A479B9C55DFCEF6A4E4AF; _csrf=ebf6ff89afbf5b791a2de53c842d221b5f100406beb141fbc73c5ca2e3e606e6; _lxsdk_cuid=172ef0ce8e7c8-06a45034ef70ec-f7d1d38-16e360-172ef0ce8e7c8; _lxsdk=FA517ED0B76B11EA9B3075693A212BAF86111DE4D58A479B9C55DFCEF6A4E4AF; mojo-uuid=6ebbd31b9ad2b20a9ca98ee8d16f0a4d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593148500,1593446849; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593879443; __mta=220469159.1593148502368.1593148615270.1593879443669.10; _lxsdk_s=1731ad818e4-155-aa3-8d4%7C%7C1'
    for line in a.split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        cookiename, value = line.strip().split('=', 1)
        cookies[cookiename] = value  # 为字典cookies添加内容
    # print(cookies)

    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象
    # star_requests()方法读取 start_urls列表中的url并生成 request对象，发送给 引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        # print(self.cookies)
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse2, dont_filter=False, cookies=self.cookies)


# 整理获取到的类型字符串

    def type_text(self, typestring):
        updated = typestring.strip().split('\n')[-1].strip()
        return updated

# 解析函数 bs解析
    def parse(self, response):
        print('parse1')
        # items = []
        # print('parsing~~~~~')
        soup = BeautifulSoup(response.text, 'html.parser')
        tags = soup.find_all('div', attrs={'class': 'movie-hover-info'})
        # 切片限定爬取数量Top10
        for i in tags[0:10]:
            dtags = i.find_all('div', attrs={'class': 'movie-hover-title'})
            for j in dtags:
                item = SpidersItem()
                if j.find('span').text == '类型:':
                    movie_type = self.type_text(j.text)
                if j.find('span').text == '上映时间:':
                    movie_showtime = self.type_text(j.text)
                    movie_title = j.get('title')
                    item['mtitle'] = movie_title
                    item['mtype'] = movie_type
                    item['mshowtime'] = movie_showtime
                # print(item)
                # items.append(item)
        # print('Finished parsing~~~~~')
        # return items
                yield item

# 用Selector解析
    def parse2(self, response):
        #Selector
        print('parse2')
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        # print(len(movies))
        # 切片限定爬取数量Top10
        for movie in movies[0:10]:
            item = SpidersItem()
            # print(movie)
            movie_title = movie.xpath('./div[1]/@title').extract_first()
            # print(movie_title)
            movie_type = movie.xpath('./div[2]/text()[2]').extract_first().strip()
            # print(movie_type)
            movie_showtime = movie.xpath('./div[4]/text()[2]').extract_first().strip()
            # print(movie_showtime)
            item['mtitle'] = movie_title
            item['mtype'] = movie_type
            item['mshowtime'] = movie_showtime
            # print(item)
            yield item