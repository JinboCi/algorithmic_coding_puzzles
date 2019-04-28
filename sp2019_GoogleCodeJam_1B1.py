# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:54:31 2019

@author: cijin
"""
import numpy as np
T = int(input())

for i in range (T):
    tmp = input()
    tmparr = tmp.split()
    P = int(tmparr[0])
    Q = int(tmparr[1])
    ##print(Q)

    arr = np.zeros((Q+1,Q+1))
    for j in range(P):
        tmp = input()
        tmparr = tmp.split()
        x = int(tmparr[0])
        y = int(tmparr[1])
        D = tmparr[2]
        if (D == 'N'):
            for h in range(Q+1):
                for k in range(y+1,Q+1):
                    arr[h][k] +=1
                    
        if (D == 'S'):
            for h in range(Q+1):
                for k in range(y):
                    arr[h][k] +=1
        if (D == 'E'):
            for h in range(x+1,Q+1):
                for k in range(Q+1):
                    arr[h][k] +=1
        if (D == 'W'):
            for h in range(x):
                for k in range(Q+1):
                    arr[h][k] +=1
    maxNum = np.amax(arr) 
    lowestx = Q
    lowesty = Q           
    for h in range(Q+1):
        for k in range(Q+1):
            if (arr[h][k] == maxNum) & (h <= lowestx):
                if (k <= lowesty):
                    lowestx = h
                    lowesty = k
                
                
    print("Case #%d: %d %d" %(i+1, lowestx, lowesty))
