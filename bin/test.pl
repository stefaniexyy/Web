#!/usr/bin/perl
use strict;
use warnings;
use 5.010;

my $str="b'GET /res/aeroplane_backgroud.jpg HTTP/1.1\r\nHost: 192.168.1.129:8080\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://192.168.1.129:8080/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,es;q=0.6\r\n\r\n";
#my($a,$b)=($str)=~/^b\'(.[,3])\s(\/.*)\sHTTP/;
my($a,$b)=($str)=~/^b\'(.+)\s(\/.*)\sHTTP/;

say $a;
say $b;