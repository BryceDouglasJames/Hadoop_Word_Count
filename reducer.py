#!/usr/bin/env python3
from collections import defaultdict
import sys

#KEY: word  VALUE: amount of occurences
word_count = defaultdict(int)

for line in sys.stdin:
    try:
        #take in stdin as string and split by line
        line = line.strip()
        word, count = line.split()

        #Get amount value and increment dictionary val
        count = int(count)
        word_count[word] += count
    except:
        continue

#pipe output
for word, count in word_count.items():
    print(word, count)