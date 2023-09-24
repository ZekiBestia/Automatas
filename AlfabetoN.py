# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def asignarN(alfabeto, palabra):
    alfabeto = {letter: idx + 1 for idx, letter in enumerate(alfabeto)}
    num = 0
    for letter in palabra:
        if letter in alfabeto:
            num = num * len(alfabeto) + alfabeto[letter]
    return num

alfabeto = ['a', 'b','c','d']
palabra = "dcdab"

num = asignarN(alfabeto, palabra)
print(f'La palabra "{palabra}" tiene el número {num}')

def buscarP(alfabeto, num):
    alfabeto = {idx + 1: letter for idx, letter in enumerate(alfabeto)}
    palabra= ""
    long = len(alfabeto)

    while num > 0:
        r = (num - 1) % long
        palabra= alfabeto[r + 1] + palabra
        num = (num - 1) // long

    return palabra

alfabeto = ['a', 'b','c','d']

num = 45279
palabra = buscarP(alfabeto, num)
print(f'El número {num} corresponde a la palabra "{palabra}"')



