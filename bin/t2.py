#!//usr/bin/python
# -*- coding: utf8 -*-
import json
import re
import sys
import pymysql

pymysql.install_as_MySQLdb()

db = pymysql.connect("192.168.1.128","xyy","xyy","myblog" )
cursor = db.cursor()
cursor.execute("select * from SYS_USER")
data = cursor.fetchone()
print(data[3])
db.close()