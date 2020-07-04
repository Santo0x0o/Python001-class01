# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class SpidersPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        # print('pipelines')
        #用Pandas保存item记录为csv文件
        movie=[[item['mtitle'],item['mtype'],item['mshowtime']]]       
        movies_df = pd.DataFrame(movie, columns=[
                                'Movie_title', 'Movie_type', 'Movie_showtime'])
        movies_df.to_csv('../../../MaoyanTop10MoviesInfo_V2.csv', mode='a', index=False, header=False,encoding='UTF-8')
        # print('信息保存成功.')       
        return item