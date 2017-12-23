# -*- coding: utf-8 -*-
import scrapy


class WoaiwojiaSpider(scrapy.Spider):
    name = 'woAiWoJia'
    allowed_domains = ['https://hz.5i5j.com/zufang']
    start_urls = ['http://https://hz.5i5j.com/zufang/']

    def parse(self, response):
        pass
