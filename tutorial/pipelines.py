# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from tutorial.items import AddressItem, LianJiaItem
from pymongo.errors import DuplicateKeyError
from scrapy.log import logger


class MongoPipeline(object):
    collection_address_name = 'address'
    collection_house_name = 'house'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, AddressItem):
            item['city'] = "杭州"
            item['cityPinyin'] = 'hz'
            try:
                self.db[self.collection_address_name].insert(dict(item))
            except DuplicateKeyError:
                logger.warn("此item已经存在了！")
        elif isinstance(item, LianJiaItem):
            self.db[self.collection_house_name].insert(dict(item))
        return item

if __name__ == "__main__":
    client = pymongo.MongoClient("localhost")
    db = client["rent"]["house"]
    db.insert({"a":"b"})
