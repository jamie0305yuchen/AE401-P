# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:29:32 2021

@author: Jamie
"""

score=[['a',80],['b',90],['c',100]]
m = 0;
m_index = 0 
for i in range(0,3,1):
    if(m<score[i][1]):
        m_index = i
        m = score[i][1]
print(score[m_index][0],m)
m = 1000;
m_index = 1000 
for i in range(0,3,1):
    if(m>score[i][1]):
        m_index = i
        m = score[i][1]
print(score[m_index][0],m)