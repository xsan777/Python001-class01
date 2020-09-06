import scrapy
import pandas as pd
import collections
from snownlp import SnowNLP
from scrapy.selector import Selector
from qipaoshui.items import QipaoshuiItem

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com/fenlei/qipaoshui/']
    start_urls = ['http://smzdm.com/fenlei/qipaoshui//']

    # def parse(self, response):
    #     pass
    
    # 初始化函数，只执行一次
    def start_requests(self):
        self.n = 0
        self.targrt = []
        self.key = {}
        self.link_max = {}
        for i in range(1,4):
            url = f'https://www.smzdm.com/fenlei/qipaoshui/p{i}/#feed-main'
            yield scrapy.Request(url = url, callback = self.parse,dont_filter = True)
        
    # 解析函数
    def parse(self, response):
        item = QipaoshuiItem()
        links = Selector(response=response).xpath('//li[@class="feed-row-wide"]/div/div[1]/a/@href').extract()
        for i in range(0,len(links)):
            item['sum_i'] = 0
            yield scrapy.Request(url = links[i], meta = {'item': item,'link': links[i]}, callback = self.parse2,dont_filter = True)
    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        link = response.meta['link']
        self.n += 1
        print('n = ',self.n)
        # xml化处理
        sum_i = 0
        datas = Selector(response=response).xpath('//li[@id="li_comment"]/div[2]/div[1]/div[1]/meta/@content').extract()
        for j in range(1,len(datas)+1):
            estimates = pd.Series( Selector(response=response).xpath('//span[@itemprop="description"]/text()').extract())
            def _sentiment(text):
                return SnowNLP(text).sentiments
            for i in range(0,len(estimates)):
                estimate = estimates[i].strip()
                if len(estimate) == 0:continue
                sentiment = _sentiment(estimates[i])
                sum_i += sentiment // 0.2 + 1
                # 单商品的最后一条评论时做单商品的数据标定和请求最大评论数的前十条评论数据
                if i == len(estimates)-1 and j == len(datas) :
                    self.link_max[sum_i] = link
                    self.key = collections.OrderedDict(sorted (self.link_max.items(), reverse=True))
                    # for i in sorted (self.link_max, reverse=True):
                    #     self.key[i] = self.link_max[i]
        if self.n == 90:
            print('-'*50)
            print(self.key)
            for val in self.key.values():
                self.targrt.append(val)
            for i in range(0,10): 
                yield scrapy.Request(url = self.targrt[i], meta = {'item': item,'link': self.targrt[i]}, callback = self.parse3,dont_filter = True)
                   
    def parse3(self, response):
        item = response.meta['item']
        link = response.meta['link']
        print('+'*50)
        # xml化处理
        sum_i = 0
        datas = Selector(response=response).xpath('//li[@id="li_comment"]/div[2]/div[1]/div[1]/meta/@content').extract()
        for j in range(1,len(datas)+1):
            date=  Selector(response=response).xpath(f'//li[@id="li_comment"][{j}]/div[2]/div[1]/div[1]/meta/@content').extract_first()
            if len(date) == 0:continue
            estimates = pd.Series( Selector(response=response).xpath('//span[@itemprop="description"]/text()').extract())
            def _sentiment(text):
                return SnowNLP(text).sentiments
            if len(datas) == 0 : item['sum_i'] = 0
            for i in range(0,len(estimates)):
                estimate = estimates[i].strip()
                if len(estimate) == 0:continue
                sentiment = _sentiment(estimates[i])
                item['link'] = link
                item['date'] = date
                item['n_star'] = sentiment // 0.2 + 1
                sum_i += item['n_star']
                item['estimate'] = estimate
                item['sentiment'] = sentiment
                item['sum_i'] = sum_i
                yield item