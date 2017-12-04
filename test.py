from spider import Spider
from book import Book
from lxml import etree
import re

mySpider = Spider()
book = Book()
book.url = "https://www.amazon.cn/%E5%84%92%E6%9E%97%E5%A4%96%E5%8F%B2-%E5%90%B4%E6%95%AC%E6%A2%93/dp/B001PBEZM2/ref=sr_1_47/461-7948441-9812635?s=books&ie=UTF8&qid=1512105473&sr=1-47"


html = mySpider.loadPage("https://www.amazon.cn/%E5%84%92%E6%9E%97%E5%A4%96%E5%8F%B2-%E5%90%B4%E6%95%AC%E6%A2%93/dp/B071RFQMCG/ref=lp_659379051_1_3?s=books&ie=UTF8&qid=1512021546&sr=1-3")
res = re.compile(r'bookDescEncodedData = "(.*)",')
result = res.search(html)
print(html)

print(result.group(1))
# xpath_str = etree.HTML(html)
# xml = etree.tostring(xpath_str)
# selector = etree.HTML(xml)
# title = selector.xpath(r'//h1[@id="title"]/span[@id="productTitle"]/text()')[0]
# author = selector.xpath(r'//div[@id="byline"]//a/text()')
# authors = ""
# for a in author:
#     authors += a + ";"
#
# publication_date = selector.xpath(r'//h1[@id="title"]/span[last()]/text()')[0]
#
# price = selector.xpath(r'//div[@id="tmmSwatches"]//li[@class="swatchElement selected"]//span[@class="a-size-base a-color-price a-color-price"]/text()')[0]
#
# key = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li/b/text()')
# value = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li/text()')
#
# dic = dict(zip(key, value))
# if "丛书名:" in dic:
#     li2 = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li[2]/a/text()')[0]
#     dic["丛书名:"] = li2
#
# print(dic)
#
# print(title)



# for k, v in key, value:
#     print("key:"+ k+",value:" + v)
# # print(publish_company)
# for i in publish_company:
#
#     ml = etree.HTML(etree.tostring(i))
#     print(etree.tostring(ml))
#     emp = ml.xpath(r'//li/b/text()')[0]
#     if (emp.strip() == "出版社"):
#         print(emp)
    # print(i.strip())

# books_name = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li[2]/a/text()')[0]

# print(books_name)
# print(title)
# print(authors)
# print(publication_date)
# print(price.strip())
import urllib.parse
str = "%E4%B8%80%E9%83%A8%E5%86%99%E9%80%8F%E4%B8%AD%E5%9B%BD%E5%8F%A4%E4%BB%A3%E5%AE%98%E5%9C%BA%E7%9A%84%E7%99%BE%E7%A7%91%E5%85%A8%E4%B9%A6%E5%BC%8F%E5%B0%8F%E8%AF%B4%EF%BC%9A%3Cbr%3E%20%E6%89%A7%E9%87%91%E6%9D%AF%E9%A5%AE%E9%85%92%E7%9A%84%E7%8B%82%E7%8B%B7%E5%84%92%E5%A3%AB%EF%BC%8C%E5%8F%AA%E8%BA%AB%E9%80%83%E5%A9%9A%E7%9A%84%E5%8F%9B%E9%80%86%E6%89%8D%E5%A5%B3%EF%BC%8C%E9%85%B7%E7%88%B1%E7%94%B7%E9%A3%8E%E7%9A%84%E5%90%8D%E9%97%A8%E5%9F%BA%E5%8F%8B%EF%BC%8C%E9%9A%90%E5%B1%85%E5%B1%B1%E6%9E%97%E7%9A%84%E7%9C%9F%E5%84%92%E8%B4%A4%E4%BA%BA%EF%BC%8C%E6%AD%BB%E7%A3%95%E7%A7%91%E8%80%83%E7%9A%84%E5%93%AD%E5%8F%B7%E7%AB%A5%E7%94%9F%EF%BC%8C%E6%8B%9B%E6%91%87%E6%92%9E%E9%AA%97%E7%9A%84%E5%86%92%E7%89%8C%E8%AF%97%E4%BA%BA%EF%BC%8C%E5%8A%9D%E5%A5%B3%E6%AE%89%E5%A4%AB%E7%9A%84%E7%A4%BC%E6%95%99%E7%8B%82%E5%BE%92%EF%BC%8C%E4%BB%8E%E6%B7%B3%E6%9C%B4%E4%B8%8A%E8%BF%9B%E7%9A%84%E5%AD%9D%E5%AD%90%E5%8F%98%E4%B8%BA%E8%B4%AA%E5%A9%AA%E8%99%9A%E4%BC%AA%E7%9A%84%E5%8D%91%E9%84%99%E4%B9%8B%E5%BE%92%E2%80%A6%E2%80%A6%3Cbr%3E%20%E5%85%A8%E4%B9%A6%E6%9C%89%E5%90%8D%E6%9C%89%E5%A7%93%E7%9A%84%E4%BA%BA%E7%89%A9%E5%A4%9A%E8%BE%BE%E4%B9%9D%E5%8D%81%E5%A4%9A%E4%BD%8D%EF%BC%8C%E4%B8%80%E5%BC%A0%E5%BC%A0%E9%9D%A2%E5%AD%94%E4%BC%BC%E6%9B%BE%E7%9B%B8%E8%AF%86%EF%BC%8C%E4%B8%80%E4%B8%AA%E4%B8%AA%E6%95%85%E4%BA%8B%E7%8B%AC%E7%AB%8B%E5%8F%88%E7%B2%BE%E5%BD%A9%EF%BC%8C%E8%AF%BB%E8%B5%B7%E6%9D%A5%E8%BD%BB%E6%9D%BE%E7%95%85%E5%BF%AB%EF%BC%8C%E7%8A%B9%E5%A6%82%E8%BA%AB%E4%B8%B4%E5%85%B6%E5%A2%83%E3%80%82"
print(urllib.parse.unquote(str))