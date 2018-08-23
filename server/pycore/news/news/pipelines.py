# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import psycopg2


from scrapy.conf import settings
# from scrapy.extensions import DropItem


class MongoDBPipline(object):
    """docstring for MongoDBPipline"""

    def __init__(self):
        connection = pymongo.MongoClient(
            settings["MONGODB_SERVER"], settings["MONGODB_PORT"])
        db = connection[settings["MONGODB_DB"]]
        self.connection = db[settings["MONGODB_COLLECTION"]]

    def process_item(self, item, spider):
        self.connection.insert(dict(item))

        return item


class PostgresPipline(object):
    """docstring for PostgresPipline"""

    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host='localhost', database='twodays',
            user='admin', password='123456')
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into twodays_news(title,url,date) values(%s, %s, %s)",
                         (item['title'], item['url'], item['date']))
        self.connection.commit()

        return item
