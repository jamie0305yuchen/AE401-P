# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 10:32:54 2021

@author: Jamie
"""

import random
num=random.randint(1,20)
user=int(input())
if user < num:
    user=int(input())
print("太小")
elif user > num:
    user=int(input())
print("太大")
else :
    print("答對了")
