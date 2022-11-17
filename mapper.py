#!/usr/bin/env python3 
import sys 
import string 
import re
for line in sys.stdin: 
    
    
    try:
        #take in stdin as string and split by line
        line = line.strip() 
        words = line.split() 

        for w in words: 
            #if word is not a digit
            if not any([char.isdigit() for char in w]):
                w = w.lower()

                #if word is similar to 'and/or'
                for ans in re.split("/", w):

                    #DISGUSTING regex I am so sorry
                    ans = re.sub(r"\.\[.*\]|\.|\;|\,|\[.*\]|\:[.?*]|\:.|\(|\)|\"|\:", "", ans)
                    
                    #pipe output
                    print(ans, '\t', '1')
    except:
        continue