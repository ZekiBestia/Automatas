#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:15:38 2023

@author: zekibestia
"""

alfa = ['a','b','c','d']
pal = "bbcdcacc"
m = len(alfa)
n = len(pal)
print(m)
print(n)
s=((m**n) - (1) )/(m-1)
print(s)

alfa={letra: indice for indice,letra in enumerate(alfa)}
print(alfa)
valor_numerico = 0
cambiar=[]
for letra in pal:
    if letra in alfa:
        valor_numerico = alfa[letra]
        cambiar.append(valor_numerico)
cambiar=''.join(map(str,cambiar))
print(cambiar)
q=int(cambiar,m)
print(f"Valor de q: {q}")

resultado=s+q
print(resultado)

            
            
            


    