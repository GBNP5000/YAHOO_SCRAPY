import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess


class YahooSpider(CrawlSpider):
    name = 'yahoo'
    allowed_domains = ['in.yahoo.com/']
    # start_urls = ['https://in.yahoo.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'),
             callback='parse_item', follow=True),
    )

    start_urls = (
        'https://in.yahoo.com/'
    )

    # meta={
    #             'splash': {
    #                 'endpoint': 'render.html',
    #                 'args': {'wait': 0.5}
    #             }
    #         }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse_item(self, response):
        item = {}
        item['title'] = response.css('title::text').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item


process = CrawlerProcess()
process.crawl(YahooSpider)
process.start()
