#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:17:40 2021

@author: sk
"""


def comb(l,k):
    if k == 1:
        return [ [li] for li in l]
    else:
        return [ [l[i]]+j for i in range(len(l)) for j in sub(l[i+1:],k-1)]
    
def sub(l,k):
    res = []
    for i in range(len(l)-k+1):
        res.append(l[i:i+k])
    return res

def sublis(l):
    return [s for k in range(1,len(l)) for s in sub(l,k)]

def rep(l,k):
    if k == 0: return []
    else: return l+rep(l,k-1)
    
def conca(l):
    res = []
    for li in l:
        res+=li
    return res

def todas(l):
    res = []
    for s in sublis(l):
        for k in range(len(l)+1):
            if rep(s,k) == l:
                res.append([s,k])
    return res





    
def parte(l):
    return [ [l[:i]]+[l[i:]] for i in range(len(l)+1) if l[:i] != [] and l[i:] != []]+[l]
    #return res + [l]
    #return [ [l[:i]]+[l[i:]] for i in range(1,len(l)) ]

def to(l):
    if len(l)==1:
        return [[l]]
    if len(l)==2:
        return parte(l)
    else:
        return [ [l[:i]]+k for i in range(1,len(l)) for k in to(l[i:]) ]+[l]
    

def trozos(l):
    return [ [l[:i]]+k for i in range(1,len(l)+1) for k in trozos(l[i:]) if l[:i] != [] and l[i:] != []]+[[l]]

    

    
#comprime debil
def compri(l):
    res = []
    for i in range(1,int(len(l)/2)+1):
        for k in range(1,int(len(l)/i)+1 ):
            #print(l[:i], k, " veces == ", rep(l[:i],k) )
            if rep(l[:i],k) == l:
                res.append([l[:i],k])
    #return res
    return res[0] if len(res)>0 else [l,1]



            
            
def comprime(l):
    res = []
    for t in trozos(l):
        #print("voy con particion ", t)
        este = []
        for ti in t:
            #print("    comprimo ", ti)
            este.append(compri(ti))
        res.append(este)
    return comprimecomprime(corta(res))
            
def lcompresion(l):
    res = 0
    for li in l:
        res+=len(li[0])
    return res


# [ [l0,k],[l1,k],... ]
def corta(l):
    mj = l[0]
    for li in l:
        if lcompresion(li)<lcompresion(mj):
            mj = li
    return mj



def comprimecomprime(l):
    res = ""
    def compi(l):
        txt = ""
        if len(l[0])==1:
            txt+="("+str(l[0][0])+")"
            txt+=str(l[1])
        else:
            txt+="("
            for li in l[0]:
                txt+=str(li)
            txt+=")"
            txt+=str(l[1])
        return txt
    for li in l:
        res+=compi(li)
    return res
        
            
                
        
    

l = [1,1,1,2,1,2,1,2,1,2,1,1,1,2,2]
print(l,"  COMPRIMIDA:  ", comprime(l))
        
  
    