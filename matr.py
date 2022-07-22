#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 23:11:02 2021

@author: sk
"""

import random
import numpy as np



def ver(m):
    for mi in m:
        print(mi)
        

def encode(m):
    ia = []
    io = []
    for i in range(len(m)):
        pon = 0
        for j in range(len(m[i])):
            if j<i:
                if m[i][j]!=0 or pon: 
                    ia.append(m[i][j])
                    pon=1
            if i==j:
                ia.append(m[i][j])
                io.append(len(ia)-1)
    return ia,io


def mult(M):
    ia, io, x = M
    res = []
    [res.append(0) for _ in range(len(io))]
    arriba, abajo = 0, 0
    j = 0
    # solo para saber como seria matriz sin 0s (para ver cuantos se salta (por 0s))
    def num(n):
        ress = [0]
        paso = 2
        for _ in range(n-1):
            ress.append(ress[-1]+paso)
            paso+=1
        return ress
    
    sucesion = num(len(io))
    
    # bucle ia
    for i in range(len(ia)):
        if i != io[j]: # no sume 2 veces
            res[arriba] += x[abajo]*ia[i] 
        res[abajo] += x[arriba]*ia[i]
        
        arriba+=1
        if i == io[j]: # si diagonal
            if  j<len(io)-1: 
                arriba =  ((sucesion[j+1]-sucesion[j]) - (io[j+1] - io[j])) 
            else: arriba = 0
            abajo+=1
            j+=1
    return res


# crea matrices random simetricas con bastantes 0os    
def matr(n): 
    matrix = []
    [matrix.append([0 for _ in range(n)]) for _ in range(n)]
    
    for i in range(n): 
         
        f = random.randint(0, n-1)
        c = random.randint(0, n-1)
        el = random.randint(0, 9)
        matrix[f][c] = el
        matrix[c][f] = el
        
        matrix[i][i]=random.randint(1, 9) 
        
    
    
    return matrix
        
    
# tester
def test(n):
    # matriz random
    M = matr(n)
    
    # por el cual multilicarla
    x = []
    [x.append(random.randint(1, 9)) for _ in range(n)]
    
    # encodeo
    ia, io = encode(M)
    
    # comparacion con numpy 
    print(mult([ia,io,x])," == ",np.matmul(M,x)," :", mult([ia,io,x])==np.matmul(M,x))
    
    return 


    
    
[test(k) for k in range(1,7) for _ in range(10) ] # 7 dimension maxima matrices, 10 vueltas

a1 = [[1,1,2,0,1],[0,1,4],[1,1,1]] # [3,1,3]

a2 = [[1,2,1,3,4,1,5,6,7,1],[0,2,5,9],[1,1,1,1]] # [11, 13, 15, 19]
        
            
a3 = [[1,1,2,3,1,4,5,1],[0,1,4,7],[1,1,1,1]] # [3,8,11,10]
            
a4 = [[1,2,1,3,1,4,1,5,6,7,8,1],[0,2,4,6,11],[1,1,1,1,1]] # [8, 12, 15, 13, 27]


m1 = [[1,0,2,0],[0,1,3,4],[2,3,1,5],[0,4,5,1]] # [1, 1, 2, 3, 1, 4, 5, 1], [0, 1, 4, 7]