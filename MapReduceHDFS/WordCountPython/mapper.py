V#!/usr/bin/env python
"""mapper.py"""
from sys import stdin
import re
import os

id = 0
for line in stdin:
    id = id + 1
    docId = "{}{}".format("doc", id)
    words = re.findall(r'\w+', line.strip())
    wordNum = 0
    for word in words:
        wordNum = wordNum + 1
        print("%s\t%s:%s" % (word.lower(), docId, str(wordNum)))
    # Get the file path
