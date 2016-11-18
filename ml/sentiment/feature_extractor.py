# -*- coding: utf-8 -*- #

import jieba
import logging
import os

logger = logging.getLogger(__name__)

class FeatureExtractor(object):

    def __init__(self):
        resources_path = os.path.dirname(__file__) + "/resources"
        self._stopwords = None
        self._locs = None

        try:
            with open(resources_path + "/stopwords.txt", "r") as infile:
                self._stopwords = {line.decode("utf-8") for line in infile}

            with open(resources_path + "/loc.txt", "r") as infile:
                self._locs = {line.decode("utf-8") for line in infile}
        except Exception as e:
            logger.info(repr(e))


    def is_valid_word(self, word):
        if word in self._stopwords or word in self._locs:
            return False
        else:
            return True

    def extract(self, raw_data):
        words = jieba.cut(raw_data)

        words = [word for word in words if self.is_valid_word(word)]

        return words
