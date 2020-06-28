import scrapy
from spiders.items import MaoYanItem
from scrapy.selector import Selector
class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movives = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        i = 1
        for movive in movives:
            movie_name = movive.xpath('.//span/text()')
            movie_type = movive.xpath('.//div[@class="movie-hover-title"]/text()')
            movie_up_time = movive.xpath('.//div[@class="movie-hover-title movie-hover-brief"]/text()')
            items = MaoYanItem()
            items['movie_name'] = movie_name.extract_first().strip()
            items['movie_type'] = movie_type.extract()[4].strip()
            items['movie_up_time'] = movie_up_time.extract()[1].strip()
            i += 1
            if i >10:
                break
            yield items

