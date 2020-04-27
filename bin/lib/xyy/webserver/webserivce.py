#!/usr/bin/python
import sys
import re

class WebServer:
    def __init__(self):
        self.http_ok_image="HTTP/1.1 200 OK\r\nContent-Type: image/jpg\r\n\r\n"
        self.http_ok_css="HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"
        self.http_ok_html="HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        self.http_ok_file="HTTP/1.1 200 OK\r\nContent-Type: application/ttf\r\n\r\n"
        self.http_fail_html="HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        self.http_fail_image="HTTP/1.1 404 Not Found\r\nContent-Type: image/jpg\r\n\r\n"
        self.http_fail_css="HTTP/1.1 404 Not Found\r\nContent-Type: text/css\r\n\r\n"


    def test(self):
        return self.http_ok_image 

    def Retrun_response(self,file_name):
        #Here transsfer front page to a normal page
        file_name=file_name if file_name !='/' else '/main.html'
        response=""
       
        if re.search(r'jpge$|jpg$|png$|bmp$|webp$|ico$',file_name,re.M|re.I):#Picture
            response=self.process_image(file_name)
        elif re.search(r'css$',file_name,re.M|re.I):#CSS
            response=self.process_css(file_name)
        elif re.search(r'html|htm$',file_name,re.M|re.I):#html
            response=self.process_html(file_name)
        elif(r'ttf|otf$',file_name,re.M|re.I):
            response=self.process_fontfile(file_name)
        
        return response

    def process_html(self,filename):
        response_start_line=""
        response_body=""
        try:
            file=open('../src/html'+filename,'rb')
            #print('../src/html'+filename)
            response_body=file.read()
            file.close()
            response_start_line=self.http_ok_html
        except IOError:
            response_start_line = self.http_fail_html
            response_body=bytes('<h1>Error 404 Page Lost</h1>',"gb2312")
        return bytes(response_start_line,"gb2312") + response_body
        
    def process_image(self,filename):
        response_start_line=""
        response_body=""
        try:
            file=open('../src'+filename,'rb')
            response_body=file.read()
            file.close()
            response_start_line=self.http_ok_image
        except IOError:
            response_start_line = self.http_fail_image
            response_body=bytes('',"gb2312")
        return bytes(response_start_line,"gb2312") + response_body

    def process_css(self,filename):
        response_start_line=""
        response_body=""
        try:
            file=open('../src'+filename,'rb')
            response_body=file.read()
            file.close()
            response_start_line=self.http_ok_css
        except IOError:
            response_start_line = self.http_fail_css
            response_body=bytes('',"gb2312")
        return bytes(response_start_line,"gb2312") + response_body

    def process_fontfile(self,filename):
        response_start_line=""
        response_body=""
        try:
            file=open('../src'+filename,'rb')
            response_body=file.read()
            file.close()
            response_start_line=self.http_ok_file
        except IOError:
            response_start_line = self.http_fail_image
            response_body=bytes('',"gb2312")
        return bytes(response_start_line,"gb2312") + response_body

    def handle_client(self,client_socket):#parameter 1=client_socket
        """
        处理客户端请求
        """   
        response_headers = ""
        request_data = client_socket.recv(1024)
        request_Info=re.search(r'^b\'(.+) (\/[\.\/\w\W\d]*) HTTP\/',str(request_data),re.M|re.I)
        try:
            request_type=request_Info.group(1)#
            request_file=request_Info.group(2)#file name
        except AttributeError:
            print(request_Info)
        #response=self.Create_Staic_Page(request_file)
        response=self.Retrun_response(request_file)
        client_socket.send(response)
        client_socket.close()
        return request_Info