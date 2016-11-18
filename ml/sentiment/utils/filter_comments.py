# -*- coding: utf-8 -*- #
# Author: Jiaquan Fang

import os
import sys
import traceback

def filter_nonchinese(text):
    _MIN_CHINESE_UNICODE = u'\u4e00'
    _MAX_CHINESE_UNICODE = u'\u9fa5'

    characters = [ch for ch in text if ch >= _MIN_CHINESE_UNICODE and
                                ch <= _MAX_CHINESE_UNICODE]

    return "".join(characters)


class CommentFilter(object):

    def __init__(self):
        resources_path = "../resources"
        self._poswords = None
        self._negwords = None

        try:
            with open(resources_path + "/poswords.txt", "r") as infile:
                self._poswords = {line.decode("utf-8").rstrip("\n")
                                  for line in infile}

            with open(resources_path + "/negwords.txt", "r") as infile:
                self._negwords = {line.decode("utf-8").rstrip("\n")
                                  for line in infile}

        except:
            traceback.print_exc()


    def is_positive(self, data):
        pos_count = 0
        neg_count = 0
        for word in self._poswords:
            if word in data:
                pos_count += 1

        for word in self._negwords:
            if word in data:
                neg_count += 1

        if pos_count > neg_count:
            return True
        else:
            return False


if __name__ == "__main__":
    f = CommentFilter()

    positive_comments = []
    negative_comments = []
    try:
        with open(sys.argv[1], "r") as infile:
            for line in infile:
                line = line.decode("utf-8").rstrip("\n").split("\t")[1]

                if f.is_positive(line):
                    positive_comments.append(line)
                else:
                    negative_comments.append(line)


        with open("pos.txt", "w") as outfile:
            for line in positive_comments:
                outfile.write(
                    filter_nonchinese(line).encode("utf-8") + "\n")

        with open("neg.txt", "w") as outfile:
            for line in negative_comments:
                outfile.write(
                    filter_nonchinese(line).encode("utf-8") + "\n")

    except:
        traceback.print_exc()


