#!/usr/bin/env python

#print('Привет мир')
import copy;

f = open('zdb.utf8.txt','r');

phrase = "ростелеком"
d = {}
for i in range(0,len(phrase)):
    symbol = phrase[i]
    if symbol in d:
        d[symbol]+= 1
    else :
        d[symbol] = 1
#print(d)

res = []
for i in f:
    i = i.strip()
    if len(i) <= 2:
        continue
    a = copy.copy(d)
    letter_not_found = 0;
    for j in range(0,len(i)):
        letter = i[j]
        if letter in a:
            a[letter] -= 1
            if a[letter] == 0:
                del a[letter]
        else :
            letter_not_found = 1
            break
    if letter_not_found == 0 :
        print(i)
        res.append(i)

#print(res)

