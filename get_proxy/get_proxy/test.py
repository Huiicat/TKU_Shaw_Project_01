import pymongo
import requests

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["IT_db"]
mycol = mydb["IT_coll"]

mydict = [{ "name": "John", "address": "Highway 37" },{ "name": "Hannah", "address": "Mountain 21"}]

# for i in mydict:
#     print(i)
#     print(mycol.find_one({"name":i['name']}))
#     if mycol.find_one({"name":i['name']}):
#         print('pass')
#         pass
#     else:
#         print('insert')
#         x = mycol.insert_one(i)

for x in mycol.find():
    print(x['name'])
    mycol.delete_one(x)
    
# url = 'https://httpbin.org/ip'
# old_proxy = 'https://167.172.140.184:3128'
# headers = {"User-Agent": "Mozilla/5.0"}
# res = requests.get(url, proxies={'https':old_proxy}, headers=headers)
# if res.status_code == 200:
#     print(res)
# else:
#     print('no')

    # collection_name = 'pool'

    # def __init__(self, mongo_uri, mongo_db):
    #     self.mongo_uri = mongo_uri
    #     self.mongo_db = mongo_db

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )

    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]

    # def close_spider(self, spider):
    #     self.client.close()

    # def process_item(self, item, spider):
    #     # if self.db[self.collection_name].find({"proxy": item['proxy']}):
    #     #   print('pass:'+item['proxy'])
    #     #   pass
    #     # else:
    #     #   print('insert:'+item['proxy'])
    #     self.db[self.collection_name].insert_one(dict(item))
    #     return item

#      def __init__(self):
#    pass
#   self.connect = pymysql.connect(
#   #  host = settings.MYSQL_HOST,
#   #  db = settings.MYSQL_DBNAME,
#   #  user = settings.MYSQL_USER,
#   #  passwd = settings.MYSQL_PASSWD,
#    host = '127.0.0.1',
#    db = 'ip_proxy_pool',
#    user = 'root',
#    passwd = '0000',
#    port = 3306,
#    charset = 'utf8',
#    use_unicode = True
#   )
#   self.cursor = self.connect.cursor(); 
#  def process_item(self, item, spider):
#   try:
#     count = self.cursor.execute( "select count(*) from pool")
#     scheme = self.cursor.execute( "select scheme from pool")
#     proxy = self.cursor.execute( "select proxy from pool")
#     port = self.cursor.execute( "select port from pool")
#     # item['scheme'] = self.cursor.execute( "select scheme from pool")
#     # item['proxy'] = self.cursor.execute( "select proxy from pool")
#     # item['port'] = self.cursor.execute( "select port from pool")
#     for i in range(count):
#       match_object = re.search(r"(http|https)://(.+):", proxy)
#       ip = match_object.group(2)
#       meta = {
#           'port': port[i],
#           'proxy': proxy[i],
#           'dont_retry': True,
#           'download_timeout': 5,
#           '_proxy_scheme': scheme[i],
#           '_proxy_ip': ip
#       }
#       # print(meta)
#       yield scrapy.Request('https://httpbin.org/ip',callback=self.proxy_checkagain, meta=meta, dont_filter=True)

#     self.cursor.execute("select * from pool where proxy = %s",item['proxy'])

#     repetition = self.cursor.fetchone()

#     if repetition:
#       pass
#     else:
#       self.cursor.execute(
#       "insert into pool (scheme, proxy, port) value(%s, %s, %s)",
#       (item['scheme'],
#         item['proxy'],
#         item['port']
#         # item['update']
#         ))
#       self.connect.commit()
#   except Exception as error:
#    logging.log(error)
#   return item
#   def proxy_checkagain(self, response):
#         json_data = json.loads(response.text)['origin']
#         proxy_ip = response.meta['_proxy_ip']+', '+response.meta['_proxy_ip']
#         if proxy_ip != json.loads(response.text)['origin']:
#             yield self.cursor.execute( "delete * from pool where proxy=%s",response.meta['proxy'])
#             self.connect.commit()
#  def close_spider(self, spider):
#   self.connect.close();