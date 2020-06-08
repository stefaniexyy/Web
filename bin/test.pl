#!/usr/bin/perl
use strict;
use warnings;
use 5.010;


my $a='stefaniexyy@hotmail.com';
say $a;
if($a=~/^[\w_\.-]+[\w_\.-]*@[\w_\.-]+[\w_\.-]*\.[a-zA-Z]+$/){
    say 'OK';
}else{
    say 'Fail';
}