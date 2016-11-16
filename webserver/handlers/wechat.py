import json
import tornado.web

import hashlib
import logging
from handlers.base import BaseHandler

class WeChatTokenHandler(BaseHandler):

    def get(self):
        signature = self.get_argument("signature", default=None, strip=True)
        timestamp = self.get_argument("timestamp", default=None, strip=True)

        nonce = self.get_argument("nonce", default=None, strip=True)
        echostr = self.get_argument("echostr", default=None, strip=True)

        token="q1w2E#R$"
        l = [token, timestamp, nonce]
        l.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, l)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr

