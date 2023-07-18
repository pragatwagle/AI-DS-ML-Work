#!/usr/bin/env python
"""reducer.py"""
from sys import stdin
import re

index = {}

for line in stdin:
        wordAndPosting = line.split('\t')
        # get the word
        word = wordAndPosting[0]
        # get posting which coutains 1 and WordIndex separated by :
        postings = wordAndPosting[-1].strip()
        #set default as word and an empty dictionary which will be indexed by
        #document eg. [word][doc]
        index.setdefault(word, {})
        #split the posting to get to doc id and word index in document
        doc_idAndWordLoc = postings.split(':')
        #get the doc
        doc_id = doc_idAndWordLoc[0]
        #get the word location or index in document
        word_loc = doc_idAndWordLoc[-1]
        #set default it it does not exist, the second parameter is [count, [arrayofwordindexlocations]]
        index[word].setdefault(doc_id, [0,[ ]])
        #increment the count by 1 based on the word and document
        index[word][doc_id][0] += 1
        #append the word location in document to index of word and doc id indexed array
        index[word][doc_id][1].append(word_loc)
#format of output
print("WORD tab {Document1:[Count, [WordIndexs]]...DocumentN:[Count, [WordIndexs]]}")
for word in index:
    print('%s\t%s' % (word, index[word]))
