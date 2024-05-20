# -*- coding: utf-8 -*-
import scrapy
import time
from fake_useragent import UserAgent

class RecetaspiderSpider(scrapy.Spider):
    name = 'recetaspider'
    #allowed_domains = ['https://www.recetasgratis.net/']
    start_urls = ['https://www.recetasgratis.net/recetas-peruanas']
    # TIME_SLEEP = 2
    
    agent = UserAgent()
    custom_settings = {
        'USER_AGENT': agent.random
    }

    def start_requests(self):
        # generates multiple requests from text file
        start_urls = open('../data/raw/links_cousines.txt').read().splitlines()
        for url in start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        # print(response.request.headers)
        # set the category
        categoria = response.url.split('-')[1]

        # collect the urls, pass the category and make a request
        urls = response.css('div[class="resultado link"] > a::attr(href)').extract()
        for url in urls:
            newurl = response.urljoin(url)
            yield scrapy.Request(url=newurl, callback=self.parse_details, meta={'categoria': categoria})

        # don't be mad, add some time
        # time.sleep(self.TIME_SLEEP)

        # navigation through pages
        next_page_url = response.css('div.paginator > a[class="next ga"]::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        """ function that extract details info
        # KEYPOINT: the space in label selects texts and text links in tags
        """
        yield{
            'categoria': response.meta['categoria'],
            'receta': response.css('h1::text').extract_first(),
            'fecha': response.css('div.nombre_autor > span::text').extract_first(),
            'autor': response.css('div.nombre_autor > a::text').extract_first(),
            'valoracion': response.css('div.daticos > a > span::text').extract_first(),
            'propiedades': ','.join(response.css('div.properties > span::text').extract()),
            'ingredientes': ','.join(response.css('li.ingrediente > label ::text').extract()),
        }


