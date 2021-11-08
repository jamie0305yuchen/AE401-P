# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:42:43 2021

@author: Jamie
"""

m=int(input())
e=int(input())
if m>89 and e>89:
    print("有獎品")
elif m>59 or e>59:
    print("在加油")
else:
    print("要處罰")