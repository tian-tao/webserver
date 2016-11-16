from handlers.base import BaseHandler

import logging

class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")
