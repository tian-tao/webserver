# -*- coding: utf-8 -*- #
# Author: Jiaquan Fang

import sys

def filter_nonchinese(text):
    _MIN_CHINESE_UNICODE = u'\u4e00'
    _MAX_CHINESE_UNICODE = u'\u9fa5'

    characters = [ch for ch in text if ch >= _MIN_CHINESE_UNICODE and
                                ch <= _MAX_CHINESE_UNICODE]

    return "".join(characters)


reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    s = u"一般"
    print filter_nonchinese(s)
