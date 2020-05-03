#!//usr/bin/python
import json
from self import *


class class_A:
    def __init__(self):
        pass

    def func1(self,par1):
        return fun1


class b:
    def __int__(self):
        self.a1=a(self)
    
    def func2(self):
        return self.a1.func1('Hello')


test=b()
print(test.func2())