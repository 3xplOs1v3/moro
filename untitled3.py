#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:19:52 2021

@author: sk
"""
from numpy.random import random, normal, choice, uniform

def suma(lista):
    valor = 0
    for x in lista:
        valor += x 
    return valor


def sumar(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0]+sumar(lista[1:])
        

"""
sumar([1,2,3])
    lista[0] # es el 1
    sumar([2,3])
        lista[0] # es el 2
        sumar([3])
            lista[0] # es el 3
            sumar([])
                return 0
        
"""

"""
funcion(parametro)
    caso base
    funcion(parametroNuevo)
"""


def cuantos(elem,lista):
    c = 0
    for l in lista:
        if l==elem:
            c+=1
    return c

def cuantosr(elem, lista):
    #caso base
    if len(lista)==0:
        return 0 
    elif lista[0]==elem:
        return 1+cuantosr(elem,lista[1:])
    else:
        return cuantosr(elem, lista[1:])
    




def maximo(lista):
    maxi = lista[0]
    for l in lista:
        if l>maxi:
            maxi = l
    return maxi
  
# O(n)
def maxii(lista):
    maximo = lista[0]
    j = 0
    for i in range(len(lista)):
        if lista[i]>maximo:
            maximo = lista[i]
            j = i
    return j
        
       
# O(n**2)
def ordena(lista):
    lista2 = []
    for _ in range(len(lista)):
        pos = maxii(lista)
        lista2.append(lista[pos])
        lista = lista[:pos]+lista[pos+1:]
    return lista2


# devuelve la pos del elem en lista
def posi(elem,lista):
    print(lista)
    if elem==lista[int(len(lista)/2)]:
        return int(len(lista)/2)
    elif len(lista)==1: 
        return -999
    elif elem<lista[int(len(lista)/2)]:
        return int(len(lista)/2) + posi(elem,lista[int(len(lista)/2):])
    else:
        return posi(elem,lista[:int(len(lista)/2)])
        
    


def bubl(lista):
    for _ in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i+1]<lista[i]:
                tmp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = tmp
    return lista





def merge(lista):
    if len(lista)==0: return []
    m = lista[int(len(lista)/2)]
    left, right = [], []
    for l in lista:
        if l<m:
            left.append(l)
        elif l>m:
            right.append(l)
    return merge(left)+[m]+merge(right)

#norep
def mergee(lista):
    return [] if len(lista)==0 else merge([k for k in lista if k<lista[int(len(lista)/2)]])+[lista[int(len(lista)/2)]]+merge([k for k in lista if k>lista[int(len(lista)/2)]])

# mapa 
# [1,2,2,3,6,4,4,8,8,8,9]
# [ [1,1], [2,2], [3,1], [4,2], [8,3], [9,1] ]
def mapa(lista):
    res = []
    for l in lista:
        contador = 0
        for li in lista:
            if l == li:
                contador+=1
        if [l,contador] not in res: res.append([l,contador])
    return res


"""
trios(1):
    [0,0,1]
    [0,1,0]
    [1,0,0]

trios(2):
    [0,0,2]
    [0,1,1]
    [0,2,0]
    [1,0,1]
    [1,1,0]
    [2,0,0]
"""
def trios(n):
    res = []
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if i+j+k==n:
                    res.append([i,j,k])
    return res





# 


#def to(m,n):
#    return [ [k] for k in range(n+1)] if m ==1 else [ [k]+j for k in range(n+1) for j in to(m-1,n)]
    

#def mn(m,n):
#    return [ r for r in to(m,n) if sum(r)==n ]


# xke puta
#def to(m,n):
#    return [ [k] for k in range(n+1)] if m ==1 else [ [k]+j for k in range(n+1) for j in to(m-1,n) if sum([k]+j)==n ]
    
    



def mn(m,n):
    return [ [k] for k in range(n+1)] if m ==1 else [ [k]+j for k in range(n+1) for j in mn(m-1,n-k) if sum([k]+j)==n ]
   



# palabras de longitud m que sumen n
"""
def mn(m,n):
    if m == 1:
        return [ [k] for k in range(n+1)]
    else:
        return [ [k]+j for k in range(n+1) for j in mn(m-1,n)]
"""      
        


def fact(n):
    return 1 if n==1 else n*fact(n-1)


def formula(m,n):
    return int(fact((n+m-1))/(fact(n)*fact(m-1)))



    
    
    
    
    
    
    
    
    
    


"""
palabras([a,b,c,d],1): [a], [b], [c], [d]
palabras([1,2,3],2) # habra len**2

    11
    21
    31
    
    12
    22
    32
    
    13
    23
    33
    
"""
def palabras(elementos, longitud):
    if longitud==1:
        return [[e] for e in elementos]
    return [ [e]+i  for e in elementos for i in palabras(elementos,longitud-1)]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    