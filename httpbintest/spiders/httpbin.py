# -*- coding: utf-8 -*-
import logging

import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        self.logger.debug(response.text)
        self.logger.debug('Status Code:' + str(response.status))



# 设置代理
# class ProxyMiddleware(object):
#     logger = logging.getLogger(__name__)
#     def process_request(self, request, spider):
#         self.logger.debug('Using Proxy')
#         request.meta['proxy'] = 'http://'
