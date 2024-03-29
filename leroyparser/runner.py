from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from Lesson_6.leroyparser.spiders.leroymerlin import LeroymerlinSpider
from Lesson_6.leroyparser import settings

query = 'брус'

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpider, search_string=query)

    process.start()