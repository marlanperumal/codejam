import scrapy

class ScoreboardSpider(scrapy.Spider):
    name = "scoreboard"

    def start_requests(self):
        urls = ["https://codejam.withgoogle.com/2018/challenges/0000000000007883/scoreboard"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
