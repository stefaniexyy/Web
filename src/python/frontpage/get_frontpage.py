#!/usr/bin/python
# -*- coding: utf8  -*-
import sys
import json
sys.path.append('../src/python/frontpage')
sys.path.append('.')
from head import *
from content import *
from tail import *

class get_page:
        def generate_full_page(self):
                head_objet=get_head()
                content_object=get_content()
                full_page="""<html>"""+head_objet.head_content()+content_object.body_content()+"""
</html>"""
                return full_page

        
class post:
        def login_request(self,content):
                print('content is:'+content)
                content_json=json.loads(content)
                if content_json['username']=='sysadmin' and content_json['password']=='11':
                        resulut='{"login_result":"succ"}'
                else:
                        resulut='{"login_result":"fail"}'
                return resulut


#a=get_frontpage()
#b=a.generate_full_page()
#print(bytes(b,'utf8'))