import scrapy


class Part2spiderSpider(scrapy.Spider):
    name = "part2spider"
    allowed_domains = ["simplyhired.com"]
    start_urls = ["https://simplyhired.com"]

    def parse(self, response):
        pass
