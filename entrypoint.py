# -*-coding: utf-8 -*-

from scrapy.cmdline import execute


def run_spider(spider_name):
    """
    执行爬虫
    :param spider_name: 爬虫名称
    :return: None
    """
    execute(['scrapy', 'crawl', spider_name])

if __name__ == "__main__":
    run_spider("LJSpider")
