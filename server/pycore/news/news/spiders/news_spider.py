import scrapy
import random

class NewsSpider(scrapy.Spider):
	"""docstring for NewsSpider"""
	name = "news"

	def start_requests(self):
		

