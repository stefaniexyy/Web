#!/usr/bin/python
import time

hash_a={}
hash_a['1']=[]
hash_a['1'].append('a')
hash_a['1'].append(1)
hash_a['1'][1]=hash_a['1'][1]+1
print(hash_a['1'][1])