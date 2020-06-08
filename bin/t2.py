#!//usr/bin/python
# -*- coding: utf8 -*-
import json
import re
import sys
import pymysql

#pymysql.install_as_MySQLdb()
db_str=["192.168.1.128","xyy","xyy","myblog"]
db = pymysql.connect(db_str[0],db_str[1],db_str[2],db_str[3])
cursor = db.cursor()
cursor.execute("select PROLE from SYS_USER where user_name=\'YY\' and password=\'XYY\'")
data = cursor.fetchone()
result= 'fail' if data is None else 'succ'
db.close()
print(result)