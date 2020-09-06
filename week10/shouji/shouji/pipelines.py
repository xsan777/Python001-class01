# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
# 执行批量插入
# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)

class ShoujiPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = '123456',
                        database = 'django',
                        charset = 'utf8mb4'
                        )
        sql = 'DROP TABLE shouji_shouji;'
        sql1 = ''' CREATE TABLE IF NOT EXISTS `shouji_shouji`(
                `id` INT UNSIGNED AUTO_INCREMENT,
                `date` varchar(30) not null,
                `n_star` int(5) not null,
                `estimate` varchar(200) NOT NULL,
                `sentiment` decimal(11,10) not null,
                PRIMARY KEY ( `id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''
                # 'INSERT `qipaoshui_qipaoshui` SELECT * FROM `qipaoshui_base` GROUP BY RAND();'
        sql2 = "INSERT INTO `shouji_shouji`(`date`, `n_star`, `estimate`, `sentiment`) VALUES ('{date}','{n_star}', '{estimate}', '{sentiment}')".format(date=item['date'], n_star=item['n_star'], estimate=item['estimate'], sentiment=item['sentiment']);
        
        try:
            # 获得cursor游标对象
            con1 = conn.cursor()
            # 操作的行数
            con1.execute(sql)
            con1.execute(sql1)
            con1.execute(sql2)
            conn.commit()
        except Exception as e:
            print(sql1)
            print(e,'操作失败====================================')
        con1.close()
        conn.close()
        return item 