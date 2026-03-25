import scrapy


class WikiResultItem(scrapy.Item):
    status = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    tooltip = scrapy.Field()
    url = scrapy.Field()
    results = scrapy.Field()
