#!/bin/python
import re

def get_post_object(post_content):
        print('post_content is:'+post_content)
        """
            解析post消息，返回一个二维数组
            [请求的key，请求的value]
        """
        arr_content=post_content[:-1].split('&')
        arr_return=[]
        for i in arr_content:
            content=re.search(r'^([\d\w_]+)=(.+)$',i,re.M|re.I)
            arr_return.append([content.group(1),content.group(2)])
        return arr_return
        
        
    