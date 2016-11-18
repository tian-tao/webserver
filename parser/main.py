# -*- coding: utf-8 -*-

from lib.crawl_full_page import crawl
from lib.get_product_price import get_price
from lib.get_shop_rate import get_shop_rate

from bs4 import BeautifulSoup
import json

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

