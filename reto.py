#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:11:49 2021

@author: sk
"""




"""
1 2 3 
4 5 6 
7 8-1
tablero = [3,6,4,5,-1,7,8,2,1]
movimiento = [1,2]

[]
0 1 2
3 4 5
6 7 8

"""

N = 3

goal = [1,2,3,4,5,6,7,8,-1]


def printea(tablero):
    k = 1
    s = "|"
    print("-------")
    for t in tablero:
        if t==-1: t=" "
        s = s+str(t)+"|"
        if k%N == 0:
            print(s)
            s = "|"
        k+=1
    print("-------")
        
def mueve(movimiento, tableroo):
    # [1,2] pos!
    tablero = tableroo.copy()
    t = tablero[movimiento[0]]
    tablero[movimiento[0]] = tablero[movimiento[1]]
    tablero[movimiento[1]] = t
    return tablero
    
def hueco(tablero):
    pos = 0
    for t in tablero:
        if t==-1: 
            return pos
        pos+=1
    return pos

def posibles(tablero):
    res = []
    pos = hueco(tablero)
    
    if pos==0:
        res.append([pos,1])
        res.append([pos,3])
    if pos==2:
        res.append([pos,1])
        res.append([pos,5])
    if pos==6:
        res.append([pos,3])
        res.append([pos,7])
    if pos==8:
        res.append([pos,5])
        res.append([pos,7])
    if pos==4:
        res.append([pos,1])
        res.append([pos,3])
        res.append([pos,5])
        res.append([pos,7])
    if pos==1:
        res.append([pos,0])
        res.append([pos,2])
        res.append([pos,4])
    if pos==3:
        res.append([pos,0])
        res.append([pos,4])
        res.append([pos,6])
    if pos==5:
        res.append([pos,2])
        res.append([pos,4])
        res.append([pos,8])
    if pos==7:
        
        
        res.append([pos,4])
        res.append([pos,6])
        res.append([pos,8])
        
    return res

    
def ejecuta(tablero, path, historico):
    if tablero==goal:
        print("yeah",path)
        print("historico: ",historico)
        return path
    if len(path)>20:
        return
    s = posibles(tablero)
    
    return [ejecuta(mueve(si,tablero),path+[si],historico+[mueve(si,tablero)]) for si in s if mueve(si,tablero) not in historico]
    
def sol(tablero,movs):
    printea(tablero)
    for m in movs:
        print("X por ",tablero[m[1]]) 
        tablero = mueve(m,tablero)
        printea(tablero)
        print("\n")
