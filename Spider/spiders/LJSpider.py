# -*-coding: utf-8 -*-
"""
杭州链家爬虫
"""
import scrapy

from scrapy.http import Request
from lxml.html import etree
from Spider.items import AddressItem
from Spider.items import LianJiaItem
from Spider.utils import PinyinUtil


class LJSpider(scrapy.Spider):
    name = "LJSpider"
    allowed_domains = ['hz.lianjia.com']
    start_urls = ['https://hz.lianjia.com/zufang/']
    base_url = 'https://hz.lianjia.com/zufang/'
    pinyin = PinyinUtil()

    def parse(self, response):
        """
        解析出最大页数, 并按页请求
        :param response: 请求start_urls获得的response
        """
        html = response.text
        max_page = self.parse_max_page(html)
        for page in range(1, max_page + 1):
            url = self.base_url + "pg" + str(page) + "/"
            yield Request(url, callback=self.parse_list_page)

    def parse_list_page(self, response):
        """
        解析列表页面, 获得详情页面的url, 并请求详情页面
        :param response: 按页请求获得的response
        """
        html = response.text
        detail_url_list = self.parse_detail_list(html)
        for url in detail_url_list:
            yield Request(url, callback=self.parse_detail_page)

    def parse_detail_page(self, response):
        """
        解析详情页面
        :param response: 请求详情页面获得的response
        :return: 解析之后的item
        """
        html = response.text
        addressItem = AddressItem()
        selector = etree.HTML(html)
        div_zf_room = selector.xpath("//div[@class='zf-room']")[0]
        region = div_zf_room.xpath("//p[7]/a[1]/text()")[0]
        board = div_zf_room.xpath("//p[7]/a[2]/text()")[0]
        estate = div_zf_room.xpath("//p[6]/a[1]/text()")[0]
        addressItem['region'] = region
        addressItem['board'] = board
        addressItem['estate'] = estate
        addressItem['regionPinyin'] = self.pinyin.get_initial_pinyin(region)
        addressItem['boardPinyin'] = self.pinyin.get_initial_pinyin(board)
        addressItem['estatePinyin'] = self.pinyin.get_initial_pinyin(estate)
        lianjiaItem = LianJiaItem()
        yield addressItem

    @staticmethod
    def parse_max_page(html):
        """
        解析出最大页数
        :param html: 请求首页获得的response
        :return: 该网站的最大页数
        """
        selector = etree.HTML(html)
        result = selector.xpath('//div[@comp-module="page"]/@page-data')
        return eval(result[0])["totalPage"]

    @staticmethod
    def parse_detail_list(html):
        """
        解析出详情页面
        :param html:
        :return:
        """
        selector = etree.HTML(html)
        detail_url_list = selector.xpath('//*[@id="house-lst"]/li/div[@class="pic-panel"]/a/@href')
        return detail_url_list


if __name__ == "__main__":
    from entrypoint import run_spider

    run_spider("LJSpider")
