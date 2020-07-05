# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from proxyspider import mysql_conn

connDb = mysql_conn.ConnDB(mysql_conn.dbInfo)

class ProxyspiderPipeline:
    def process_item(self, item, spider):
        print('ip:%s' % item['ip'])
        try:
            connDb.insert_ip(item['ip'])
        except Exception as e:
            print(e)
        return item
