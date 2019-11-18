# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import pymysql
import pymongo
from get_proxy import settings
import logging
import re
import json
import requests
import time

class GetProxyPipeline(object):
 def __init__(self):
   pass

class MongoPipeline(object):
    print('Pipeline')
    def open_spider(self, spider):
        # db_uri = spider.settings.get('MONGODB_URI')
        # db_name = spider.settings.get('MONGODB_DB_NAME')
        # db_coll = spider.settings.get('MONGODB_DB_COL')
        db_uri = 'mongodb://localhost:27017/'
        db_name = 'ip_proxy_pool'
        db_coll = 'pool'
        db_client = pymongo.MongoClient('mongodb://localhost:27017')
        coll = db_client[db_name][db_coll]
        self.db_client = db_client
        self.coll = coll
        url = 'https://www.google.com.tw/'
        headers = {"User-Agent": "Mozilla/5.0"}
         print('total ip : ' + str(coll.count()))
         for x in coll.find():
           try:
             res = requests.get(url, proxies={x['scheme']:x['proxy']}, headers=headers, timeout=3)
             if res.status_code == 200 :
               print('pass : '+ x['proxy'])
             else :
               print('delete : '+ x['proxy'])
               coll.delete_one(x)
           except:
             print('refuse : ' + x['proxy'])
             coll.delete_one(x)
             continue

    def process_item(self, item, spider):
        self.insert_article(item)
        return item

    def insert_article(self, item):
        if self.coll.find_one({'proxy':item['proxy']}):
          # print('<pass> : '+item['proxy'])
          self.update_article(item)
        else:
          print('<insert> : '+item['proxy'])
          item = dict(item)
          # print(item)
          self.coll.insert_one(item)

    def update_article(self,item):
        newupdate = {"$set": {'update':item['update']}}
        self.coll.update_one({'proxy':item['proxy']},newupdate)

    def delete_article(self,response):
        proxy_ip = response.meta['_proxy_ip']+', '+response.meta['_proxy_ip']
        if proxy_ip == json.loads(response.text)['origin']:
          print('delete : '+ response.meta['_proxy_ip'])
          self.coll.delete_one({'proxy' : response.meta['_proxy_ip']})

    def close_spider(self, spider):
        print('final total ip : ' + str(self.coll.count()))
        self.db_client.close()