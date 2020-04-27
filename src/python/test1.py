<<<<<<< HEAD
# coding:utf-8

import time

def application(env, start_response):

    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
=======
# coding:utf-8

import time

def application(env, start_response):

    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
>>>>>>> 5ce23d317609a49cc361e8a040216c7547c19190
    return '<h1>'+time.ctime()+'</h1>'