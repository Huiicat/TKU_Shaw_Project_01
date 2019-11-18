"# TKU_Shaw_Project_01" <br>
_尚在編寫中

資料庫：
mongoDB

安裝套件：
scrapy
BeautifulSoup
json
pymongo
re
requests

執行方法：
scrapy crawl proxy_example

簡易流程：
1. 檢驗mongoDB中的既有IP是否有效，無效則刪去
2. 至http://www.us-proxy.org/抓取新IP
3. 檢驗新IP是否有效，有效則新增至mongoDB

**目前常駐約100個可用IP**
