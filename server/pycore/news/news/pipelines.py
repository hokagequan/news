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


# class MongoDBPipline(object):
# 	def __init__(self, arg):
# 	# 	connection = pymongo.MongoClient(settings["MONGODB_SERVER"], settings["MONGODB_PORT"])
# 		# db = connection[settings["MONGODB_DB"]]
# 		# self.connection = db[settings["MONGODB_COLLECTION"]]

#     def process_item(self, item, spider):
# 		# valid = True
# 		# for data in item:
#   #   		if not data:
#   #   			valid = False
#   #   			raise DropItem("Missing {}!".format(data))
#   #   	if valid:
#   #   		self.connection.insert(dict(item))
#   #   		scrapy.log.msg("News added to MongoDB database!", level=log.DEBUG, spider=spider)

#         return item
