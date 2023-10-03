# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class alfabeto:
 @staticmethod
 def asignarN(alfabeto, palabra):
    alfabeto = {letra: idx + 1 for idx, letra in enumerate(alfabeto)}
    num = 0
    for letra in palabra:
        if letra in alfabeto:
            num = num * len(alfabeto) + alfabeto[letra]
    return num

 alfabeto = ['a','b','c','d']
 palabra = "aaa"
 num = asignarN(alfabeto, palabra)
 print(f'La palabra "{palabra}" tiene el número {num}')

 @staticmethod
 def buscarP(alfabeto, num):
    alfabeto = {idx + 1: letra for idx, letra in enumerate(alfabeto)}
    palabra= ""
    long = len(alfabeto)

    while num > 0:
        r = (num - 1) % long
        palabra= alfabeto[r + 1] + palabra
        num = (num - 1) // long

    return palabra
'''
 alfabeto = ['a', 'b','c','d']

 num = 655
 palabra = buscarP(alfabeto, num)
 print(f'El número {num} corresponde a la palabra "{palabra}"')

'''



