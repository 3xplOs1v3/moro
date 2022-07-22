#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:07:05 2021

@author: sk

"""
import numpy as np



N = 5

def mov(P):
    O = {+1,-1}
    D = {1,2}
    return [[P[0]+oi1*di1,P[1]+oi2*di2] for oi1 in O for di1 in D for oi2 in O for di2 in D if di2!=di1]

def validos(posibles, visitados):
    res = []
    for p in posibles:
        if p not in visitados and (p[0]>=0 and p[0]<N) and (p[1]>=0 and p[1]<N):
            res.append(p)
    return res
    
    

def dale(pos):
    path = [pos]
    return ejecuta(path)
    

def ejecuta(path):
    siguientes = validos(mov(path[-1]), path)
    if len(siguientes) == 0: 
        if len(path)==N**2-1:
            print("jaja ke putada")
        #print("no encontrado")
        return 
    if len(path)==N**2-1:
        print("encontrado")
        print(path+[siguientes[0]])
        return path
    return [ejecuta(path+[s]) for s in siguientes]
    #for s in siguientes:
        #print("voy a ",s)
        #return ejecuta(path+[s])
    
    
def tablero(cuadros):
    m = np.zeros( (N, N) )
    i = 1
    for c in cuadros:
        m[c[0]][c[1]] = i
        i+=1
    return m


#dale([1,1])
"""
tablero([[1, 1], [3, 0], [2, 2], [0, 3], [2, 4], [4, 3], [3, 1], [1, 0], [0, 2], [1, 4], [3, 3], [4, 1], [2, 0], [0, 1], [1, 3], [3, 4], [4, 2], [2, 1], [0, 0], [1, 2], [0, 4], [2, 3], [4, 4], [3, 2], [4, 0]])
array([[19., 14.,  9.,  4., 21.],
       [ 8.,  1., 20., 15., 10.],
       [13., 18.,  3., 22.,  5.],
       [ 2.,  7., 24., 11., 16.],
       [25., 12., 17.,  6., 23.]])
"""