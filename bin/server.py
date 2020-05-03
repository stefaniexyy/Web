#!/usr/bin/python
import socket
import sys
import json

sys.path.append('./lib/')
from multiprocessing import Process
from xyy.webserver.webserivce import  WebServer
__author__='Willy Xi'
"""
Version 0.1 Build2
20200330
"""

#def handle_client_1(*args,**kwargs):
#    def handle_client_Z(funnction):
#        if args[0]=0:
#            fun2(*args)
#        elif args[0]=1::
#            print(funnction(*args))
#        return 1
# @handle_client_1(1)   
#WebServer.handle_client()
#
#def application(environ, start_response):
#    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web'
#    print(body)
#    return [body.encode('utf-8')]

if __name__ == "__main__":
    with open('../config/.basic.json') as basic_cfg_file:
        basic_cfg=json.load(basic_cfg_file)
    
    try:
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        server_socket.bind(("", 8080))
        server_socket.listen(128)
        while True:
            client_socket, client_address = server_socket.accept()
            print("[%s, %s]用户连接上了" % client_address)
            a=WebServer(basic_cfg['loglevel'])#记得要先初始化示例，不要用perl的写法,也别忘了()
            handle_client_process = Process(target=a.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()
    except KeyboardInterrupt:
        server_socket.close()
        sys.exit(1)