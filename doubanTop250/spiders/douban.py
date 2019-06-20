# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy import Spider
from doubanTop250.items import Doubantop250Item

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        lis=response.css('.item')
        for li in lis:
            item=Doubantop250Item()
            # 利用CSS选择器获取信息
            son_url=li.css('.pic a::attr(href)').extract()
            image=li.css('.pic a img::attr(src)').extract()
            name = li.css('.info .hd span::text').extract()
            title = ''.join(name)
            info = li.css('.info p::text').extract()[1].replace('\n', '').strip()
            score = li.css('.info .rating_num::text').extract_first()
            people = li.css('.info .star span::text').extract()[1]
            words = li.css('.info .inq::text').extract_first()
            # 生成字典
            item['son_url']=son_url
            item['image']=image
            item['title'] = title
            item['info'] = info
            item['score'] = score
            item['people'] = people
            item['words'] = words
            time.sleep(2)
            request = scrapy.Request(url=item['son_url'][0],
                                     callback=self.parse_son)
            request.meta['item'] = item
            yield request
            # 获取下一页链接,并进入下一页
        next = response.css('.paginator .next a::attr(href)').extract_first()
        if next:
            url = response.urljoin(next)
            time.sleep(1)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_son(self,response):
        # 获取子页简介信息
        item = response.meta['item']
        introduction= response.css('.related-info i::text').extract()
        content=response.css('.indent .short span::text').extract()
        new_content=''.join(content).strip().replace("\n","")
        item['introduction']=introduction
        item['content']=new_content
        yield item




