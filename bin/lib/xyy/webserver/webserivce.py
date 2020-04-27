#!/usr/bin/python
import sys
import re

class WebServer:
    def handle_client(*args):#parameter 1=client_socket
        """
        处理客户端请求
        """   
        response_headers = ""
        request_data = args[0].recv(1024)
        request_Info=re.search(r'^b\'(.+) (\/[\.\/\w\W\d]*) HTTP\/',str(request_data),re.M|re.I)
        try:
            request_type=request_Info.group(1)#
            request_file=request_Info.group(2)#file name
        except AttributeError:
            print(request_Info)
        args[0].send(WebServer.Create_Staic_Page(request_file))
        args[0].close()
        return request_Info

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