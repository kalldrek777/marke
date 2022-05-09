from datetime import time
from django.db import models

import scrapy


from market777.items import Market777Item
from weapons.models import Product
from scrapy.spiders import CrawlSpider, Rule

qs = Product.objects.all()

class MarketSpider(scrapy.Spider):
    qs = Product.objects.all().order_by('date')
    name = 'market77'
    allowed_domains = ['market-csgo.com']
    #  a = 'https://aliexpress.ru/item/1005003604058587.html?_evo_buckets=165609%2C165598%2C188873%2C224373%2C176818%2C194275&_t=gps-id%3ApcJustForYou%2Cscm-url%3A1007.13562.265877.0%2Cpvid%3Af9757e5d-c1f9-48dc-9e74-d21444912bf9%2Ctpp_buckets%3A21387%230%23250274%230&gps-id=pcJustForYou&pvid=f9757e5d-c1f9-48dc-9e74-d21444912bf9&scm=1007.13562.265877.0&scm-url=1007.13562.265877.0&scm_id=1007.13562.265877.0&sku_id=12000026461797525&spm=a2g2w.home.15002.2.5a50501dABwZvn'
    start_urls = []
    for i in qs:
        start_urls.append(i.link_product)


    def parse(self, response):
        item = Market777Item()
        item['img_url'] = response.css('div.Product_Gallery__imgWrapper__9bm18 img::attr(src)').get()

        yield item


    # def start_requests(self):
    #     for page in range(1, 1 + self.pages_count):
    #         url = f'https://parsemachine.com/sandbox/catalog/?page={page}'
    #         yield scrapy.Request(url, callback=self.parse_pages)
    #
    # def parse_pages(self, response, **kwargs):
    #     for href in response.css('.product-card .title::attr("href")').extract():
    #         url = response.urljoin(href)
    #         yield scrapy.Request(url, callback=self.parse)
    #
    # def parse(self, response, **kwargs):
    #     techs = {}
    #     for row in response.css('#characteristics tbody tr'):
    #         cols = row.css('td::text').extract()
    #         techs[cols[0]] = cols[1]
    #     item = {
    #         'url': response.request.url,
    #         'title': response.css('#product_name::text').extract_first('').strip(),
    #         'price': response.css('#product_amount::text').extract_first('').strip(),
    #         'techs': techs,
    #     }
    #     yield item



    # def parse(self, response):
    #     for link in response.css('div.product-card__image-holder a::attr(href)'):
    #         yield response.follow(link, callback=self.parse_market)
    #
    #     for i in range(1,25):
    #         next_page = f'https://book24.ru/knigi-bestsellery/page-{i}/'
    #         yield response.follow(next_page, callback=self.parse)
    #
    # def parse_market(self, response):
    #     yield {
    #         'img': response.css('a.product-card__name smartLink title::text').get()
    #     }
