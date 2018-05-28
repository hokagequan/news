import scrapy
import random

class NewsSpider(scrapy.Spider):
	"""docstring for NewsSpider"""
	name = "news"
	start_urls = [
		"https://www.baidu.com",
	]

	def parse(self, response):
		