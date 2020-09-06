from PCDjango.celery import app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import emoji
import pymysql
import pandas as pd
from snownlp import SnowNLP
from .models import Phone, PhoneCPages, PhoneCDetails


@app.task()
def get_task():
    return 'test'


def wtin():
    return (time.strftime('%Y%m%d%H%M%S'))


@app.task()
def get_comments():
    try:
        # 隐藏Chrome窗口设置
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        # 打开目标页面获取前十个手机信息
        browser.get(
            'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/')
        # time.sleep(1)
        com_as = browser.find_elements_by_xpath(
            '//*[@id="feed-main-list"]/li/div/div/div/div/a[2]')
        com_as = com_as[0:10]
        com_urls = [com_a.get_attribute('href') for com_a in com_as]
        print(com_urls)
        com_titletexts = [com_a.get_attribute('onclick') for com_a in com_as]
        com_titles = [com_title.partition("'pagetitle':'")[2].partition("','商城'")[
            0] for com_title in com_titletexts]
        print(com_titles)
        # time.sleep(1)
        phone_datas = {'phone_id': [wtin()+'_'+str(i) for i in range(10)],
                       'phone_title': com_titles,
                       'phone_url': com_urls}
        phone_df = pd.DataFrame(phone_datas)
        phone_df.to_pickle('phone_basic.pkl')
        print(phone_df)
        ### 批量保存到MySQL数据库
        phone_list = []
        for i in range(len(phone_df)):
            phone = Phone(
                phone_id=phone_df.iloc[i, 0], phone_title=phone_df.iloc[i, 1], phone_url=phone_df.iloc[i, 2])
            phone_list.append(phone)
        Phone.objects.bulk_create(phone_list)

        # phone_df = pd.read_pickle('phone_basic.pkl')
        # print(phone_df)
        com_page_datas = []
        for i in range(10):
            # print(f'---------------{i}{phone_df.iloc[i,2]}---------------')

            # 获取所有评论页面
            browser.get(phone_df.iloc[i, 2])
            # time.sleep(2)
            com_pages_lis = browser.find_elements_by_xpath(
                '//*[@id="commentTabBlockNew"]/ul[2]/li/a')
            com_pages = list(set([com_page.get_attribute(
                'href') for com_page in com_pages_lis if com_page.get_attribute('href') != 'javascript:void(0);']))
            com_pages.sort(reverse=True)
            com_pages = [phone_df.iloc[i, 2]] if com_pages == [] else com_pages
            # print(com_pages)
            for n in range(len(com_pages)):
                com_page_data = [phone_df.iloc[i, 0], n+1, com_pages[n]]
                # print(com_page_data)
                com_page_datas.append(com_page_data)
            # time.sleep(2)
        phone_compage_df = pd.DataFrame(com_page_datas, columns=[
                                        'phone_id', 'comment_page_id', 'comment_page_url'])
        phone_compage_df.to_pickle('phone_comment_pages.pkl')
        print(phone_compage_df)
        ### 批量保存到MySQL数据库
        phone_page_list = []
        for i in range(len(phone_compage_df)):
            phone_page = PhoneCPages(
                phone_id=phone_compage_df.iloc[i, 0], comment_page_id=phone_compage_df.iloc[i, 1], comment_page_url=phone_compage_df.iloc[i, 2])
            phone_page_list.append(phone_page)
        PhoneCPages.objects.bulk_create(phone_page_list)

        # phone_compage_df = pd.read_pickle('phone_comment_pages.pkl')
        # print(phone_compage_df)
        comments = []
        com_nums = []
        com_phone_id = []
        com_page_id = []
        com_page_url = []
        for p in phone_compage_df.index:
            # 访问评论页面获取评论
            browser.get(phone_compage_df.iloc[p, 2])
            com_spans = browser.find_elements_by_xpath(
                '//*[@id="commentTabBlockNew"]/ul/li/div/div/div/p/span')
            ### 使用Emoji包转换Emoji表情
            comments = comments + \
                [emoji.demojize(com_span.text) for com_span in com_spans][::-1]
            com_num_spans = browser.find_elements_by_xpath(
                '//*[@id="commentTabBlockNew"]/ul/li/div[1]/span')
            com_nums = com_nums + \
                [com_num.text for com_num in com_num_spans][::-1]
            len_com_nums = len(com_num_spans)
            com_phone_id = com_phone_id + \
                [phone_compage_df.iloc[p, 0]] * len_com_nums
            com_page_id = com_page_id + \
                [phone_compage_df.iloc[p, 1]] * len_com_nums
            com_page_url = com_page_url + \
                [phone_compage_df.iloc[p, 2]] * len_com_nums
        phone_comment_datas = {'phone_id': com_phone_id,
                               'comment_page_id': com_page_id,
                               'comment_page_url': com_page_url,
                               'comment_num': com_nums,
                               'comment_detail': comments
                               }
        phone_comments = pd.DataFrame(phone_comment_datas)
        ### 用SnowNLP库做情感分析
        phone_comments['comment_sentiments'] = phone_comments['comment_detail'].apply(
            lambda x: SnowNLP(x).sentiments )
        ### 删除有空值的行
        phone_comments.dropna(axis=0, how='any', inplace=True)
        phone_comments.to_pickle('phone_comments_details.pkl')
        print(phone_comments.head(10))
        print(phone_comments.tail(10))
        ### 批量保存到MySQL数据库
        phone_comment_list = []
        for i in range(len(phone_comments)):
            phone_comment = PhoneCDetails(phone_id=phone_comments.iloc[i, 0], comment_page_id=phone_comments.iloc[i, 1], comment_page_url=phone_comments.iloc[i, 2],
                                          comment_num=phone_comments.iloc[i, 3], comment_detail=phone_comments.iloc[i, 4], comment_sentiments=phone_comments.iloc[i, 5])
            phone_comment_list.append(phone_comment)
        PhoneCDetails.objects.bulk_create(phone_comment_list)

    except Exception as e:
        print(e)
    finally:
        browser.close()
    return 'Got the comments of top 10 cellphone done!'
