# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
# from scrapy.extensions import DropItem

class MongoDBPipline(object):
	"""docstring for MongoDBPipline"""
	def __init__(self):
		connection = pymongo.MongoClient(settings["MONGODB_SERVER"], settings["MONGODB_PORT"])
		db = connection[settings["MONGODB_DB"]]
		self.connection = db[settings["MONGODB_COLLECTION"]]
	
	def process_item(self, item, spider):
		self.connection.insert(dict(item))

		return item
