#!/usr/bin/python
# -*- coding: utf8  -*-
import sys
import json
sys.path.append('../src/python/frontpage')
sys.path.append('.')
from head import *
from content import *
from tail import *
import pymysql

class get_page:
        def generate_full_page(self):
                head_objet=get_head()
                content_object=get_content()
                full_page="""<html>"""+head_objet.head_content()+content_object.body_content()+"""
</html>"""
                return full_page

        
class post:
        def __init__(self,db):
                self.db=db

        def login_request(self,content):
                content_json=json.loads(content)
                cursor=self.db.cursor()
                cursor.execute("select PROLE from SYS_USER where user_name=\'"+content_json['username']+"\' and password=\'"+content_json['password']+"\'")
                data = cursor.fetchone()
                if data is None:
                        result='{"login_result":"fail"}'
                else:
                        result='{"login_result":"succ","role":"'+data[0]+'"}'
                return result
        
        def login_register(self,content):
                content_json=json.loads(content)
                cursor=self.db.cursor()
                cursor.execute("select count(1) from SYS_USER where user_name=\'"+content_json['username']+"\'")
                data= cursor.fetchone()[0]
                if data==0:
                        #print("insert into SYS_USER values(\'"+content_json['username']+"\',\'"+content_json['password']+"\',+\'"+content_json['email']+"\',\'normal\',\'\')")
                        cursor.execute("insert into SYS_USER values(\'"+content_json['username']+"\',\'"+content_json['password']+"\',\'normal\',\'"+content_json['email']+"\',null)")
                        self.db.commit()
                        result='{"regi_fail_reason":"succ"}'
                else:
                        result='{"regi_fail_reason":"Error_User_Exists"}'
                return result


#a=get_frontpage()
#b=a.generate_full_page()
#print(bytes(b,'utf8'))