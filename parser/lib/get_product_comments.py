# -*- coding: utf-8 -*-
import random
import re

import requests
import json

import time
import sys
sys.path.append('../')
import config

from crawl_full_page import crawl
from writetofile import write_to_txt

COMMENTS_FILE = 'file/comments.list'

def get_itemId_sellerId(html):
    print u'正则匹配itemId和sellerId'
    sellerId = None
    itemId = None
    #g_config={itemId:"520962184315",sellerId:"260030441",
    # pattern = r'.*sellerId=(\d+)&amp;itemId=(\d+).*'
    pattern = r'.*itemId:"(\d+).{1,30}sellerId:"(\d+)"'
    matchObj = re.search(pattern, str(html), re.M | re.I)
    if matchObj:
        itemId = matchObj.group(1)
        sellerId = matchObj.group(2)
        print u'匹配成功'
        print "itemId : ", matchObj.group(1)
        print "sellerId: ", matchObj.group(2)
    else:
        #itemId=523362730050&sellerId=126732883
        matchObj = re.search(r'.*itemId=(\d+)&sellerId=(\d+)', str(html), re.M | re.I)
        if matchObj:
            itemId = matchObj.group(1)
            sellerId = matchObj.group(2)
            print u'匹配成功'
            print "itemId : ", matchObj.group(1)
            print "sellerId: ", matchObj.group(2)
        else:
            print "No match!!"

    return (sellerId, itemId)

def get_detail_comments(url):
    crawled_json = crawl(url, False)
    complete_json = '{' + crawled_json + '}'
    try:
        map = json.loads(complete_json, encoding='utf-8')
    except Exception:
        print u'被封了，休息一会'
        time.sleep(random.randint(1, 5))
        return {}
    return map


def get_comments(sellerId, itemId):
    if sellerId is None or itemId is None:
        return None
    url_head = "http://rate.tmall.com/list_detail_rate.htm?itemId=" + str(itemId) + "&sellerId=" + str(sellerId)
    all_content = get_detail_comments(url_head)
    if all_content.has_key("rateDetail"):
        lastPage = all_content["rateDetail"]["paginator"]["lastPage"]
        lastPage = lastPage if lastPage < config.MAX_PAGE_SIZE else config.MAX_PAGE_SIZE
    else:
        lastPage = 2
    for currentPage in range(1, lastPage):
        print u'抓取评论第' + str(currentPage) + u'页'
        print 'page = ' + str(currentPage)
        url = url_head + "&currentPage=" + str(currentPage)
        all_content = get_detail_comments(url)
        if("rateDetail" not in all_content):
            print u'抓取发生异常，跳过'
            continue
        rateList = all_content["rateDetail"]["rateList"]
        for rate in rateList:
            comments = rate["rateDate"] + '\t' + rate["rateContent"] + '\t' + url
            write_to_txt(comments, COMMENTS_FILE, rate["rateContent"] + url)
            print "rateContent = " + rate["rateDate"] + "\t" + rate["rateContent"]



if __name__ == "__main__":
    html = '<!DOCTYPE html><html class="w990 ks-webkit538 ks-webkit ks-safari2 ks-safari"><head><script charset="gbk" src="https://bar.tmall.com/cueAssetMsg.htm?sellerId=890482188&amp;itemId=540219887479&amp;brandId=&amp;frontEndCatId=&amp;bizId=&amp;bizInfo=..pc&amp;_ksTS=1479348797763_2535&amp;callback=__mallbarCueAssetMsg&amp;_input_charset=UTF-8" async=""></script><script charset="gbk" src="https://fragment.tmall.com/tmbase/mallbar_3_2_16?bizInfo=..pc&amp;_ksTS=1479348797540_2388&amp;callback=__mallbarGetConf&amp;_input_charset=UTF-8" async=""></script><script charset="gbk" src="https://bar.tmall.com/getMallBar.htm?sellerNickName=nike%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;bizInfo=..pc&amp;_ksTS=1479348797133_2375&amp;callback=__mallbarGetMallBar&amp;shopId=71955116&amp;v=3.2.4&amp;bizId=&amp;sellerId=890482188&amp;itemId=540219887479&amp;_input_charset=UTF-8" async=""></script><script charset="utf8" src="https://g.alicdn.com/sd/data_sufei/1.3.6/sufei/??sufei-min.js?t=1_2013072520131122.js" async=""></script><script src="https://amos.alicdn.com/muliuserstatus.aw?_ksTS=1479348791485_2340&amp;callback=jsonp2341&amp;beginnum=0&amp;charset=utf-8&amp;uids=nike%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&amp;site=cntaobao" async=""></script><script src="https://g.alicdn.com/aliww/web.ww.im/0.1.9/scripts/adapter.js"></script><script charset="utf-8" src="https://g.alicdn.com/??mui/mallbar/3.2.22/index.js,kissy/k/1.4.2/swf-min.js,kissy/k/1.4.2/xtemplate-min.js,kissy/k/1.4.2/xtemplate/compiler-min.js,mui/mallbar/3.2.22/conf.js,mui/mallbar/3.2.22/util.js,mui/mallbar/3.2.22/model.js,mui/mallbar/3.2.22/store.js,mui/storage/3.0.5/index.js,mui/storage/3.0.5/conf.js,mui/storage/3.0.5/util.js,mui/storage/3.0.5/xd.js,mui/storage/3.0.5/name.js,mui/mallbar/3.2.22/mallbar-item.js,mui/ma'
    html = '<script>(function(w, d) {var gt = \'getElementsByTagName\',h = d[gt](\'head\')[0],m,i;w.g_config={itemId:"520962184315",sellerId:"260030441",shopId:"58422074",startTime:(+new Date()),p:1,type:"b",t:"2013072520131122",assetsHost:"//assets.alicdn.com",pw:(window.screen.width >= 1260&&true&&(4222&8||4222&512||4222&16384||(/standard=1/.test(window.location.search)&&!false)))?"1190":"990",webww:true,removeBrandBar:true,ap_mods:{jstracker:[0]},"loadModulesLater":true,shopUrl:"//reddragonfly.tmall.com",moduleTimeStamp: ""  ,showDetailQrcode:true,showShopQrcode:true,wtId:"2048020261",reviewsVersion:"3.0.6",beautyBucketTestIdArray:"[all]",cspuBucketTestIdArray:"[all]",monthlySalesBucketTestIdArray:"[no]",beautyVesion :"1.4.2",controlModuleOwn:"true",toolbar:false,ueUrl:"//feedback.taobao.com/pc/feedbacks?productId=339&source=Web",shopVersion:"3.1.126",tmShopAges: 8 ,ueId:1677,\n        \t\t\t\t                        <script>(function(w, d) {var gt = \'getElementsByTagName\',h = d[gt](\'head\')[0],m,i;w.g_config={itemId:"537827738349",sellerId:"387195437",shopId:"60842662",startTime:(+new Date()),p:1,type:"b",t:"2013072520131122",assetsHost:"//assets.alicdn.com",pw:(window.screen.width >= 1260&&true&&(4222&8||4222&512||4222&16384||(/standard=1/.test(window.location.search)&&!false)))?"1190":"990",webww:true,removeBrandBar:true,ap_mods:{jstracker:[0]},"loadModulesLater":true,shopUrl:"//gnshijia.tmall.com",moduleTimeStamp: ""  ,showDetailQrcode:true,showShopQrcode:true,wtId:"2070703777",reviewsVersion:"3.0.6",beautyBucketTestIdArray:"[all]",cspuBucketTestIdArray:"[all]",monthlySalesBucketTestIdArray:"[no]",beautyVesion :"1.4.2",controlModuleOwn:"true",toolbar:false,ueUrl:"//feedback.taobao.com/pc/feedbacks?productId=339&source=Web",shopVersion:"3.1.126",tmShopAges: 7 ,ueId:1677,\n        \t\t\t\t                        <script>(function(w, d) {var gt = \'getElementsByTagName\',h = d[gt](\'head\')[0],m,i;w.g_config={itemId:"537827738349",sellerId:"387195437",shopId:"60842662",startTime:(+new Date()),p:1,type:"b",t:"2013072520131122",assetsHost:"//assets.alicdn.com",pw:(window.screen.width >= 1260&&true&&(4222&8||4222&512||4222&16384||(/standard=1/.test(window.location.search)&&!false)))?"1190":"990",webww:true,removeBrandBar:true,ap_mods:{jstracker:[0]},"loadModulesLater":true,shopUrl:"//gnshijia.tmall.com",moduleTimeStamp: ""  ,showDetailQrcode:true,showShopQrcode:true,wtId:"2070703777",reviewsVersion:"3.0.6",beautyBucketTestIdArray:"[all]",cspuBucketTestIdArray:"[all]",monthlySalesBucketTestIdArray:"[no]",beautyVesion :"1.4.2",controlModuleOwn:"true",toolbar:false,ueUrl:"//feedback.taobao.com/pc/feedbacks?productId=339&source=Web",shopVersion:"3.1.126",tmShopAges: 7 ,ueId:1677,'
    (sellerId, itemId) = get_itemId_sellerId(html)
    print (sellerId, itemId)
    # get_comments(sellerId, itemId)
