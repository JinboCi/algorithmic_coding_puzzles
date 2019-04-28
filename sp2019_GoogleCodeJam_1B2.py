# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 02:03:56 2019

@author: cijin
"""
import math


tmp = input()
tmparr = tmp.split()
T = int(tmparr[0])
W = int(tmparr[1])

for i in range(T):
    print(60)
    res1 = int(input())
    print(185)
    res2 = int(input())
    for j in range(W-1):
        print(0)
        tmp = input()
    R1 = 0
    R2 = 0
    R3 = 0
    R4 = 0
    R5 = 0
    R6 = 0
    if (res1 >= 2**60):
        R1 = (int) (res1/2**60)
        res1 -= 2**60
    if (res1 >= 2**30):
        R2 = (int) (res1/2**30)
        res1 -= 2**30
    if (res2 >= 2**61):
        R3 = (int) (res2/2**61)
        res2 -= 2**61
    if (res2 >= 2**46):
        R4 = (int) (res2/2**46)
        res2 -= 2**46
    if (res2 >= 2**37):
        R5 = (int) (res2/2**37)
        res2 -= 2**37
    if (res2 >= 2**30):
        R6 = (int) (res2/2**30)
        res2 -= 2**30
    
        
    print(R1, R2, R3, R4, R5, R6)
    tmp = input()
        
