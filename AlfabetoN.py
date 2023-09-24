# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def asignarN(alfabeto, palabra):
    alfabeto = {letra: idx + 1 for idx, letra in enumerate(alfabeto)}
    print("Se le asigna valores a cada elemeto del alfabeto")
    print(alfabeto)
    num = 0
    for letra in palabra:
        if letra in alfabeto:
            num = num * len(alfabeto) + alfabeto[letra]
    return num

alfabeto = ['a','b','c','d']
palabra = "caddc"

num = asignarN(alfabeto, palabra)
print(f'La palabra "{palabra}" tiene el número {num}')

def buscarP(alfabeto, num):
    alfabeto = {idx + 1: letra for idx, letra in enumerate(alfabeto)}
    palabra= ""
    long = len(alfabeto)

    while num > 0:
        r = (num - 1) % long
        palabra= alfabeto[r + 1] + palabra
        num = (num - 1) // long

    return palabra

alfabeto = ['a', 'b','c','d']

num = 655
palabra = buscarP(alfabeto, num)
print(f'El número {num} corresponde a la palabra "{palabra}"')





