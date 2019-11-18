"# TKU_Shaw_Project_01" <br>
_尚在編寫中

資料庫：<br>
mongoDB<br>

安裝套件：<br>
scrapy<br>
BeautifulSoup<br>
json<br>
pymongo<br>
re<br>
requests<br>

執行方法：<br>
scrapy crawl proxy_example<br>

簡易流程：<br>
1. 檢驗mongoDB中的既有IP是否有效，無效則刪去
2. 至http://www.us-proxy.org/抓取新IP
3. 檢驗新IP是否有效，有效則新增至mongoDB

**目前常駐約100個可用IP**
