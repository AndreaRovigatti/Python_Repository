#!/usr/bin/python
# -*- coding: utf-8 -*
# creo oggetto mutabile:lista
print("--Creo e modifico oggetto mutabile(lista) attraverso metodo--")
lista1 = [2, 1, 3]
print(lista1 , id(lista1) , sep=':')
lista1.sort()
print(lista1 , id(lista1) , sep=':')
print("--Creo e modifico oggetto immutabile(stringa) attraverso augmented assignment--")
stringa1 = "pippo"
print(stringa1 , id(stringa1) , sep=':')
stringa1 += " baudo" #augmented assignment
print(stringa1 , id(stringa1) , sep=':')
print("--Creo e modifico 1 elemento int presente in lista attraverso augmented assignment--")
lista1 = [2, 1, 3]
print(lista1 , id(lista1) , sep=':')
lista1[1] += 1
print(lista1 , id(lista1) , sep=':')