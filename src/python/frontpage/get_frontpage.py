#!/usr/bin/python
# -*- coding: utf8  -*-
import sys
sys.path.append('../src/python/frontpage')
sys.path.append('.')
from head import *
from content import *
from tail import *

class get_frontpage:
    def generate_full_page(self):
        head_objet=get_head()
        content_object=get_content()
        full_page="""<html>"""+head_objet.head_content()+content_object.body_content()+"""
</html>"""
        return full_page

        



#a=get_frontpage()
#b=a.generate_full_page()
#print(bytes(b,'utf8'))