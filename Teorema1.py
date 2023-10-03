#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:15:38 2023

@author: zekibestia
"""

alfa = ['a','b','c','d']
pal = "dcdab"
m = len(alfa)
n = len(pal)
print(f"Palabra: {pal}")
print(f"Valor de m: {m}")
print(f"Valor de n: {n}")
s=((m**n) - (1) )/(m-1)
print(f"Valor de s: {s}")
print("Se numera las letras:")
alfa={letra: indice for indice,letra in enumerate(alfa)}
print(alfa)
valor_numerico = 0
cambiar=[]
for letra in pal:
    if letra in alfa:
        valor_numerico = alfa[letra]
        cambiar.append(valor_numerico)
cambiar=''.join(map(str,cambiar))
print(f"Convertimos letras a numeros segun la numeracion:{cambiar}")
print(f"De base {m} a decimal")
q=int(cambiar,m)
print(f"Valor de q: {q}")

resultado=s+q
print(f"Resultado de sumar {s} + {q} = {resultado}")

            
            
            


    