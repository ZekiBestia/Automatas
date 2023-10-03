#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:53:48 2023

@author: zekibestia
"""
'''
import regex as re
from automata.fa.dfa import DFA
from automata.parsers.regex import RegexParser

# Definir una expresión regular
regex_str = "(a|b)c*"

# Crear un DFA a partir de la expresión regular
parser = RegexParser()
parsed_regex = parser.parse(regex_str)
dfa = parsed_regex.to_dfa()

# Imprimir información sobre el DFA
print("Automata")
print("=======>")
print(f"Estados: {dfa.states}")
print(f"Inicial: {dfa.initial_state}")
print(f"Aceptacion: {dfa.accept_states}")
print("Transiciones: {")
for transition in dfa.transitions:
    print(f"   {transition},")
print("}")
print("=======>")

'''
from pythomata import SimpleDFA
from pythomata.automaton import Automaton
from pythomata.regex import Regex

def regex_to_dfa(regex_str):
    # Parse la expresión regular
    regex = Regex(regex_str)
    
    # Convierte la expresión regular en un DFA
    dfa = regex.to_dfa()
    
    return dfa

def print_dfa(dfa):
    print("Automata")
    print("=======>")
    print(f"Estados: {dfa.states}")
    print(f"Inicial: {dfa.initial_state}")
    print(f"Aceptacion: {dfa.accept_states}")
    print("Transiciones: {")
    for transition in dfa.transitions:
        print(f"   {transition},")
    print("}")
    print("=======>")

# Ejemplo de uso
regex_str = "(a|b)c*"
dfa = regex_to_dfa(regex_str)
print_dfa(dfa)
