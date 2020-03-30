#!/usr/bin/python
import socket
import sys
import re
from multiprocessing import Process


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
        print('request_file:'+request_file)
    except AttributeError:
        print(request_Info)
    if re.search(r'jpge$|jpg$|png$|bmp$|webp$|ico$;',request_file,re.M|re.I):
        file=open('../src'+request_file,'rb')
        data=file.read()
        response_body = data
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: image/jpg\r\n\r\n"
        client_socket.send(bytes(response_start_line,"gb2312")+data)
        client_socket.close()
        file.close()
    elif re.search(r'css$',request_file,re.M|re.I):
        file=open('../src'+request_file,'r',encoding='gb2312')
        data=file.read()
        response_body = data
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"
        response = response_start_line + response_headers+ "\r\n" + response_body
        client_socket.send(bytes(response, "gb2312"))
        client_socket.close()
        file.close()
    elif re.search(r'html|htm$',request_file,re.M|re.I) and not re.search(r'main.html',request_file,re.M|re.I):
        print('../src/html'+request_file)
        file=open('../src/html/b757.html','rb')
        data=file.read()
        response_body = data
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response =bytes(response_start_line + response_headers+ "\r\n",'gb2312') + response_body
        client_socket.send(response)
        client_socket.close()
        file.close()
    else:
        file=open('../src/html/main.html','r',encoding='gb2312')
        data=file.read()
        response_body = data
        response_start_line = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response = response_start_line + response_headers+ "\r\n" + response_body
        client_socket.send(bytes(response, "gb2312"))
        client_socket.close()
        file.close()
    #printprint("request data:", request_data)
    # 构造响应数据
    
    #response_body = "<h1>Python HTTP Test</h1>"
    
    # 向客户端返回响应数据
    #client_socket.send(bytes(response_css, "utf-8"))
    # 关闭客户端连接
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