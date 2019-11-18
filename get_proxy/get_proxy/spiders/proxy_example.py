# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import json
import time
from ..items import GetProxyItem
from ..items import PassProxyItem

class ProxyExampleSpider(scrapy.Spider):
    name = 'proxy_example'
    allowed_domains = ['www.us-proxy.org']
    start_urls = ['http://www.us-proxy.org/']

    # def start_requests(self):
    #     yield scrapy.Request('http://www.us-proxy.org/', dont_filter=True)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        trs = soup.select("#proxylisttable tr")
        for tr in trs:
            tds = tr.select("td")
            if len(tds) > 6:
                ip = tds[0].text
                port = tds[1].text
                anonymity = tds[4].text
                ifScheme = tds[6].text
                update = tds[7].text
                if ifScheme == 'yes': 
                    scheme = 'https'
                else: scheme = 'http'
                proxy = "%s://%s:%s"%(scheme, ip, port)
                meta = {
                    'port': port,
                    'proxy': proxy,
                    'dont_retry': True,
                    'download_timeout': 5,
                    '_proxy_scheme': scheme,
                    '_proxy_ip': ip,
                    'update': update
                }
                # print(meta)
                yield scrapy.Request('https://httpbin.org/ip',callback=self.proxy_check_available, meta=meta, dont_filter=True,errback = lambda x: self.download_errback(x,meta['proxy']))
                # time.sleep(3000)
        
    def proxy_check_available(self, response):
        json_data = json.loads(response.text)['origin']
        # print(json_data)
        proxy_ip = response.meta['_proxy_ip']+', '+response.meta['_proxy_ip']
        item = GetProxyItem()
        # print('proxy_ip:'+proxy_ip)
        if proxy_ip == json.loads(response.text)['origin']:
            item['scheme'] = response.meta['_proxy_scheme']
            item['proxy'] = response.meta['proxy']
            item['port'] = response.meta['port']
            item['update'] = response.meta['update']
            yield item

    def download_errback(self,e,proxy):
        # print('<error> : '+proxy)
        pass

