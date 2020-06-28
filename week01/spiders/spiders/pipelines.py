# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class SpidersPipeline:
    def process_item(self, item, spider):
        mylist = [(item['movie_name'],item['movie_type'],item['movie_up_time'])]
        movies_dataframe = pd.DataFrame(data=mylist)
        movies_dataframe.to_csv('./mymovies.csv',mode='a',encoding='utf8',index=False,header=False)
        return item
