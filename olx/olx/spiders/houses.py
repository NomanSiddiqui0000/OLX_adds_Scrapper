import scrapy
from urllib.parse import urlencode, urljoin
import time
import requests

class OlxAddsSpider(scrapy.Spider):
    name = "houses"
    allowed_domains = ["olx.com.pk"]
    start_urls = ["https://www.olx.com.pk/houses_c1721"]

    def parse(self, response):
        # print(response)
        hrefs = response.css("div.a52608cc > a::attr(href)").getall()
        base_url = response.url  # Get the base URL
        for href in hrefs:

            absolute_url = urljoin(base_url, href)
            # time.sleep(0.2)
            yield scrapy.Request(url=absolute_url, callback=self.parse_item)
        yield from self.parse_nextpage(response)

    def parse_item(self, response):
        print(response.request.headers)
        yield {
            "Title":response.css("h1.a38b8112 ::text").get(),
            "Price": response.css("span._56dab877::text").get(),
            "Seller-Name":response.css("span._6d5b4928:nth-child(1).be13fe44 ::text").get(),
            "Location":response.xpath("//div[@class='_1075545d' and .//span[@aria-label='Location']]//text()").get(),
            "Brand":response.css("div._676a547f:nth-child(3) > div:nth-child(1) > span:nth-child(2) ::text").get(),
            "Condition":response.css("div._676a547f:nth-child(4) > div:nth-child(1) > span:nth-child(2) ::text").get(),
            "Is-Deliverable":response.css("div._676a547f > div:nth-child(1) > span:nth-child(2) ::text").get(),
            "Description":response.css("._0f86855a>span ::text").get()
            
        }
    def parse_nextpage(self, response):

        for i in range(2, 50): 
            pageurl = f"https://www.olx.com.pk/houses_c1721?page={i}"
            # time.sleep(0.2)
            yield scrapy.Request(url=pageurl, callback=self.parse)