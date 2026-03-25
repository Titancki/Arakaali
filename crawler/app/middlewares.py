from scrapy import signals


class CrawlerSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        instance = cls()
        crawler.signals.connect(instance.spider_opened, signal=signals.spider_opened)
        return instance

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s", spider.name)


class CrawlerDownloaderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        instance = cls()
        crawler.signals.connect(instance.spider_opened, signal=signals.spider_opened)
        return instance

    def spider_opened(self, spider):
        spider.logger.info("Downloader ready: %s", spider.name)
