import scrapy
import random

from news.items import News

class NewsSpider(scrapy.Spider):
	"""docstring for NewsSpider"""
	name = "news"
	start_urls = [
		"http://news.baidu.com/",
	]

	def parse(self, response):
		hot_news = response.css('.hotnews')
		for news in hot_news.xpath('.//a'):
			print("***************{}".format(news.css('::text').extract_first()))
			print("***************{}".format(news.xpath('@href')))
			item = News()
			item["title"] = news.css('::text').extract_first()
			item["url"] = news.xpath('@href').extract_first()
			yield item