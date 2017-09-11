# -*- coding: utf-8 -*-
import scrapy
from ..items import RecentMovieItem


class RecentMovieSpider(scrapy.Spider):
    name = "RecentMovieSpider"
    allowed_domains = ["tvmao.com"]
    start_urls = (
        'http://www.tvmao.com/movie',
    )

    def parse(self, response):
        sub_selector = response.xpath('//div[@class="rtive"]')
        for sub in sub_selector:
            item = RecentMovieItem()
            item['movie_name'] = sub.xpath('./a/img/@alt').extract()
            yield item
            #print item['movie_name'][0].encode('utf8')
