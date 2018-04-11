# -*- coding: utf-8 -*-

from scrapy.cmdline import execute


def run_spider(spider_name):
    """
    运行爬虫
    :param spider_name: 爬虫名称
    :return 启动爬虫,下载页面, 并解析页面
    """
    execute(['scrapy', 'crawl', spider_name])


def check_spider():
    """
    检查爬虫语法是否正确
    :return:
    """
    execute(["scrapy", "check", "-l"])


def fetch_url(url):
    """
    使用下载器请求url
    :param url:请求的链接地址
    :return: 返回请求结果
    """
    execute(['scrapy', 'fetch', url])


def view_url(url):
    """
    在浏览器中打开该链接
    :param url: 链接地址
    """
    execute(['scrapy', 'view', url])


def list_spider():
    """
    列出所有爬虫
    :return:
    """
    execute(['scrapy', "list"])


def parse_html(url, callback):
    """
    请求某个链接并用callback函数来解析该页面请求到的html
    :param url: 链接地址
    :param callback: 回调函数
    :return: 解析结果
    """
    execute(["scrapy", "parse", url, callback])

if __name__ == "__main__":
    test_url = 'http://www.baidu.com'
    # fetch_url(test_url)
    # check_spider()
    # list_spider()
    view_url(test_url)