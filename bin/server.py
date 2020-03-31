#!/usr/bin/python
import socket
import sys
import re
from multiprocessing import Process
__author__='Willy Xi'
"""
Version 0.1 Build2
20200330
"""
def Create_Staic_Page(file_name):
    file_name=file_name if file_name !='/' else '/main.html'
    file_path=""
    response_start_line=""
    response_headers=""
    response_body=" "
    if re.search(r'jpge$|jpg$|png$|bmp$|webp$|ico$',file_name,re.M|re.I):
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: image/jpg\r\n\r\n"
        file_path='../src'+file_name
    elif re.search(r'css$',file_name,re.M|re.I):
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"
        file_path='../src'+file_name
    elif re.search(r'html|htm$',file_name,re.M|re.I):
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        file_path='../src/html'+file_name
    else:
        print('ELSE:'+file_path)
    try:
        file=open(file_path,'rb')
        response_body=file.read()
        file.close()
    except IOError:
        if re.search(r'html|htm$',file_name,re.M|re.I):
            response_start_line = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
            response_body=bytes('<h1>Error 404 Page Lost</h1>',"gb2312")
        else:
            print("IO ERROR can not find file:"+file_path)
    response=""
    try:
        response = bytes(response_start_line,"gb2312") + response_body
    except TypeError:
        print('TypeError:'+response_start_line)
    return response

def handle_client(client_socket):
    """
    处理客户端请求
    """   
    response_headers = ""
    request_data = client_socket.recv(1024)
    request_Info=re.search(r'^b\'(.+) (\/[\.\/\w\W\d]*) HTTP\/',str(request_data),re.M|re.I)
    try:
        request_type=request_Info.group(1)
        request_file=request_Info.group(2)
    except AttributeError:
        print(request_Info)
    client_socket.send(Create_Staic_Page(request_file))
    client_socket.close()

if __name__ == "__main__":
    try:
        server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #server_socket.settimeout(CHECK_TIMEOUT)
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        server_socket.bind(("", 8080))
        server_socket.listen(128)
        while True:
            client_socket, client_address = server_socket.accept()
            print("[%s, %s]用户连接上了" % client_address)
            handle_client_process = Process(target=handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()
    except KeyboardInterrupt:
        server_socket.close()
        sys.exit(1)