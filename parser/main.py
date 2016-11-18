# -*- coding: utf-8 -*-
import site
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
site.addsitedir(ROOT)

from lib.get_product_comments import get_comments
from lib.get_product_comments import get_itemId_sellerId
import socket
import urllib2
import parser.config
import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twisted.python.win32 import WindowsError
from lib.getrecommends import get_recommends
from lib.filter import filter_comment
from lib.newdriver import new_driver, new_proxy_driver
from lib.writetofile import write_count, get_count
from lib.parse import parse_content
from lib.geturls import get_urls
from proxy.getproxy import update_proxy_pool
import requests
from lib.crawl_full_page import crawl
from lib.writetofile import write_to_txt
import commands
from lib.get_product_price import get_price
from lib.get_shop_rate import get_shop_rate

from bs4 import BeautifulSoup
import json


def test():
    urls = get_urls()
    for url in urls:
        print url
        html = crawl(url)
        soup = BeautifulSoup(html)
        shop_rate = get_shop_rate(soup)
        print shop_rate

        # price = get_price(soup)
        # print 'min price = ' + str(price)

def get_crawled_result(url):
    res = {}
    try:
        html = crawl(url)
        soup = BeautifulSoup(html)
        price = get_price(soup)
        shop_rate = get_shop_rate(soup)
        res['price'] = price if price is not None else ''
        res['shop_rate'] = shop_rate if shop_rate is not None else ''
        print 'price = ' + str(price)
        print '店铺评价 =' + str(shop_rate)
        json_res = json.dumps(res)
    except Exception as e:
        print u'汇总信息异常，url =' + str(url)
        print e
        return json.dump({})

    return json_res

def main():
    url = "http://e22a.com/h.YLdb8E?cv=AAZeSonL&sm=398363"  #tmall
    url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.159.ogQK1s&id=536443315513&ns=1&abbucket=8"
    # url = "https://item.taobao.com/item.htm?spm=a230r.1.14.237.ogQK1s&id=523362730050&ns=1&abbucket=8#detail"
    # html = crawl(url)
    # soup = BeautifulSoup(html)
    soup = BeautifulSoup(open("file/full_page/page.tmp.taobao"))
    soup.prettify()

    #价格
    # price = get_price(soup)
    # print 'price = ' + str(price)

    #店铺评价
    shop_rate = get_shop_rate(soup)
    print shop_rate


    # price = soup.find_all("em", class_="tb-rmb-num")
    # for item in price:
    #     print item.get_text()
    # print type(price)
    # print price


    # fileName = 'file/full_page/page.tmp'
    # print u'写入临时文件'
    # write_to_txt(html, fileName, url)


    # js = commands.getstatusoutput('grep "<script>(function(w, d)" ' + fileName)
    # if len(js) < 20:
    #     js = commands.getstatusoutput('grep "sellerId" ' + fileName)
    # # commands.getstatusoutput('rm -f ' + fileName)
    #
    # # 获取销售id, 商品id
    # (sellerId, itemId) = get_itemId_sellerId(js)
    # # 获取评论并写入文件
    # get_comments(sellerId, itemId)


if __name__ == "__main__":
    # try:
    #     main()
        url = "https://detail.tmall.com/item.htm?spm=a230r.1.14.159.ogQK1s&id=536443315513&ns=1&abbucket=8"
        print str(get_crawled_result("we"))
        # test()
    # except Exception as e:
    #     print e
