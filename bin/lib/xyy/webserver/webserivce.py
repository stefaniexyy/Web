#!/usr/bin/python
import sys
import re
import os
sys.path.append('./lib/')
from xyy.webserver.basic_tool import *




class WebServer:
    def __init__(self,loglevel,db):
        self.http_ok_image="HTTP/1.1 200 OK\r\nContent-Type: image/jpg\r\n\r\n"
        self.http_ok_css="HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n"
        self.http_ok_html="HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        self.http_ok_file="HTTP/1.1 200 OK\r\nContent-Type: application/ttf\r\n\r\n"
        self.http_ok_js="HTTP/1.1 200 OK\r\nContent-Type: application/x-javascript\r\n\r\n"
        self.http_fail_html="HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        self.http_fail_image="HTTP/1.1 404 Not Found\r\nContent-Type: image/jpg\r\n\r\n"
        self.http_fail_css="HTTP/1.1 404 Not Found\r\nContent-Type: text/css\r\n\r\n"
        self.http_fail_js="HTTP/1.1 404 Not Found\r\nContent-Type: application/javascript\r\n\r\n"
        self.loglevel=loglevel
        self.db=db


    def test(self):
        return self.http_ok_image 

    def Get_response(self,file_name):
        #print("function Retrun_response working")
        #Here transsfer front page to a normal page
        file_name=file_name if file_name !='/' else '/frontpage.html'
        response=""
        print('file is'+file_name[-4:])
        if file_name[-4:].lower()=='jpge' or file_name[-4:].lower()=='.jpg' or file_name[-4:].lower()=='.png' or file_name[-4:].lower()=='.bmp' or file_name[-4:].lower()=='.ico':#Picture
            response=self.process_image(file_name)
        elif file_name[-4:]=='.css':#CSS
            response=self.process_css(file_name)
        elif file_name[-4:]=='html' or  file_name[-4:]=='.html':#html
            response=self.process_html(file_name)
        elif file_name[-4:]=='.otf' or  file_name[-4:]=='.ttf':
            response=self.process_fontfile(file_name)
        elif file_name[-3:]=='.js':
            response=self.process_javascript(file_name)
        elif file_name[-4:]=='.txt':
            response=self.process_txt(file_name)
        else:
            print('Final is:'+file_name)
            response=self.process_html('/return.html')
        return response
    
    def Post_response(self,requestion_content,parameter):
        print(requestion_content)
        arr_rqeuest=requestion_content.split('/')
        print(arr_rqeuest[2])
        sys.path.insert(1,'../src/python/'+arr_rqeuest[2][0:-5])
        module= __import__('get_'+arr_rqeuest[2][0:-5])
        post_function=module.post(self.db)#m每个网页都要实现一个post类    
        if hasattr(post_function,arr_rqeuest[3]):
            fun=getattr(post_function,arr_rqeuest[3])
            response=bytes("HTTP/1.1 200 OK\r\nContent-Type: text/json\r\n\r\n"+fun(parameter),"gb2312")
        else:
            response=bytes('HTTP/1.1 404 Not Found\r\nContent-Type: text/text\r\n\r\n<h1>Error 404 Function Not Found</h1>',"gb2312")
        return response              

    def process_html(self,filename):
        response_start_line=""
        response_body=""
        print('filename is:'+filename)
        if os.path.exists('../src/html'+filename):#如果文件存在，就使用文件，不然就使用Pythpn模块
            try:
                file=open('../src/html'+filename,'rb')
                response_body=file.read()
                file.close()
                response_start_line=self.http_ok_html
            except IOError:
                response_start_line = self.http_fail_html
                response_body=bytes('<h1>Error 404 Page Lost</h1>',"gb2312")
        else:
            sys.path.insert(1,'../src/python/'+filename[1:-5])
            module= __import__('get_'+filename[1:-5])
            a=module.get_page()
            fullpage=a.generate_full_page()
            response_start_line=self.http_ok_html
            response_body=bytes(fullpage,"gb2312")          

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

    def process_txt(self,filename):
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

    def process_javascript(self,filename):
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

    
    #decrator to control logprint, if 1 print ,0 not print
    def log_wrriter(func):
        def _wrapper(self,*args):
            result=func(self,*args)
            if self.loglevel==1:
                print(result)
            return  result
        return  _wrapper

    @log_wrriter
    def get_recive(self,client_socket):
        request_data = client_socket.recv(1024)
        return request_data
        
    def handle_client(self,client_socket):#parameter 1=client_socket
        """
        处理客户端请求
        """   
        response_headers = ""
        request_type=""
        request_file=""
        request_data=self.get_recive(client_socket)
        arr_request=[]
        arr_request=str(request_data).split('\\r\\n')
        arr_request_info=arr_request[0].split(' ')
        #print('arr_req[0] is:'+str(request_data))
        if len(arr_request_info[0])>4:#防止出响应里面只有'b 的空请求
            if arr_request_info[0][2:] == "GET":#对于GET请求，直接发送数据
                response=self.Get_response(arr_request_info[1])
                client_socket.send(response)
                client_socket.close()
            elif arr_request_info[0][2:] == "POST":
                post_into=arr_request[-1][:-1]
                response=self.Post_response(arr_request_info[1],post_into)
                client_socket.send(response)
                client_socket.close()
            else:
                print(arr_request_info[1][2:]+'|')
        return 1