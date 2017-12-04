import requests
import time
import re
from lxml import etree
import writeXLSX
from book import Book
import urllib.parse


class Spider(object):
    # 抓取网页
    def loadPage(self, url):
        print(url)

        # url = "https://www.amazon.cn/s/ref=sr_pg_" + str(page) + "?rh=n%3A658390051%2Cn%3A%21658391051%2Cn%3A658394051%2Cn%3A658511051%2Cn%3A659379051&page=" + str(page) +"&ie=UTF8&qid=1512021475"
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"

        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers = headers)

        print("status:", response.status_code)

        return response.text

    # 解析网页
    def re_html(self, html, re):
        xpath_str = etree.HTML(html)
        xml = etree.tostring(xpath_str)
        selector = etree.HTML(xml)
        getUrlList = selector.xpath(re)
        return getUrlList

    # 返回具体内容页
    def re_min_html(self, html):
        xpath_str = etree.HTML(html)
        xml = etree.tostring(xpath_str)
        selector = etree.HTML(xml)
        title = selector.xpath(r'//h1[@id="title"]/span[@id="productTitle"]/text()')[0]
        author = selector.xpath(r'//div[@id="byline"]//a/text()')
        authors = ""
        for a in author:
            authors += a + ";"

        publication_date = selector.xpath(r'//h1[@id="title"]/span[last()]/text()')[0]

        price = selector.xpath(
            r'//div[@id="tmmSwatches"]//li[@class="swatchElement selected"]//span[@class="a-size-base a-color-price a-color-price"]/text()')[
            0]

        key = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li/b/text()')
        value = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li/text()')

        dic = dict(zip(key, value))
        if "丛书名:" in dic:
            li2 = selector.xpath(r'//div[@id="detail_bullets_id"]//div[@class="content"]//li[2]/a/text()')[0]
            dic["丛书名:"] = li2

        dic["书名:"] = title.strip()
        dic["出版日期:"] = publication_date.strip()
        dic["价格:"] = price.strip()
        dic["作者:"] = authors

        # 获取简介
        res = re.compile(r'bookDescEncodedData = "(.*)",')
        result = res.search(html)
        comment = result.group(1)
        dic["内容简介:"] = urllib.parse.unquote(comment)
        return dic

def main():
    print("开始爬取文学页。。。。。。")
    mySpider = Spider()

    # 定义一个数组封装所得到的书籍信息
    bookList = []

    # 爬取5页 返回书籍URL列表
    for index in range(1, 2):
        print("正在抓取第%s页" % index)

        # 开始爬取网页
        html = mySpider.loadPage("https://www.amazon.cn/s/ref=sr_pg_" + str(
            index) + "?rh=n%3A658390051%2Cn%3A%21658391051%2Cn%3A658394051%2Cn%3A658511051%2Cn%3A659379051&page=" + str(
            index) + "&ie=UTF8&qid=1512021475")

        # 解析网页获取URL列表
        htmlList = mySpider.re_html(html, r'//div[@class="a-column a-span12 a-text-center"]/a/@href')

        # 将获取的列表封装到book类中
        for url in htmlList:
            book = Book()
            book.url = url
            # print(book)
            bookList.append(book)

    # 爬取每一个URL返回一个书籍类
    for b in bookList:
        minSpider = Spider()
        doc = {}
        # 出现错误时跳过该URL
        try:
            minhtml = minSpider.loadPage(b.url)
            doc = minSpider.re_min_html(minhtml)
        except Exception as e:
            print('Error:', e)
            continue
        print(doc)
        b.name = doc["书名:"]
        b.author = doc["作者:"]
        b.publication_date = doc["出版日期:"]
        b.price = doc["价格:"]
        b.publish_company = doc["出版社:"]
        if "丛书名:" in doc:
            b.books_name = doc["丛书名:"]
        if "ISBN:" in doc:
            b.ISBN = doc["ISBN:"]
        b.content = doc["内容简介:"]

    # 写入excel
    path = "/Users/xiesheng/PycharmProjects/amazon/古典文学" + str(int(time.time())) + ".xlsx"
    writeXLSX.write07Excel(path, bookList, "古典文学书籍")

def mainS():
    print("开始爬取生活页。。。。。。")
    mySpider = Spider()

    # 定义一个数组封装所得到的书籍信息
    bookList = []

    # 爬取5页 返回书籍URL列表
    for index in range(1, 2):
        print("正在抓取第%s页" % index)



        # 开始爬取网页
        html = mySpider.loadPage("https://www.amazon.cn/s/ref=lp_658673051_pg_" + str(
            index) + "?rh=n%3A658390051%2Cn%3A%21658391051%2Cn%3A658673051&page=" + str(
            index) + "&ie=UTF8&qid=1512393357")

        # 解析网页获取URL列表
        htmlList = mySpider.re_html(html, r'//div[@class="a-column a-span12 a-text-center"]/a/@href')

        # 将获取的列表封装到book类中
        for url in htmlList:
            book = Book()
            book.url = url
            # print(book)
            bookList.append(book)

    # 爬取每一个URL返回一个书籍类
    for b in bookList:
        minSpider = Spider()
        doc = {}
        # 出现错误时跳过该URL
        try:
            minhtml = minSpider.loadPage(b.url)
            doc = minSpider.re_min_html(minhtml)
        except Exception as e:
            print('Error:', e)
            continue
        print(doc)
        b.name = doc["书名:"]
        b.author = doc["作者:"]
        b.publication_date = doc["出版日期:"]
        b.price = doc["价格:"]
        b.publish_company = doc["出版社:"]
        if "丛书名:" in doc:
            b.books_name = doc["丛书名:"]
        if "ISBN:" in doc:
            b.ISBN = doc["ISBN:"]
        b.content = doc["内容简介:"]

    # 写入excel
    path = "/Users/xiesheng/PycharmProjects/amazon/运动健身" + str(int(time.time())) + ".xlsx"
    writeXLSX.write07Excel(path, bookList, "运动健身书籍")


if __name__ == '__main__':
    main()
    mainS()











