# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pymysql

dbInfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'TestFPy',
    'db': 'movies'
}

# sqls = ['select 1', 'select VERSION()','select * from movies.maoyaninfo;']

result = []


class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        # self.run()

    def run(self):
        conn = pymysql.Connection(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()


class SpidersPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        # print('pipelines')
        # # 用Pandas保存item记录为csv文件
        # movie = [[item['mtitle'], item['mtype'], item['mshowtime']]]
        # movies_df = pd.DataFrame(movie, columns=[
        #     'Movie_title', 'Movie_type', 'Movie_showtime'])
        # movies_df.to_csv('../../../MaoyanTop10MoviesInfo_V2.csv',
        #                  mode='a', index=False, header=False, encoding='UTF-8')
        # # print('信息保存成功.')

        # 将结果保存到MySQL
        sqls = ['INSERT INTO maoyaninfo ( mtitle, mtype, mshowtime) VALUES '+'("'+item['mtitle'] +
                '", "'+item['mtype']+'", "'+item['mshowtime']+'");', 'select * from movies.maoyaninfo;']
        db = ConnDB(dbInfo, sqls)
        db.run()
        return item
