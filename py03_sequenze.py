#!/usr/bin/python
# -*- coding: utf-8 -*
# Le sequenze(str, byte , list , tuple) sono contenitori ordinati di lunghezza arbitraria, che appartengono alla categoria
# più generica degli oggetti iterabili.Sono contenitori indicizzati iniziando da 0(elemento primo a sinistra) per proseguire verso destra.
# Gli oggetti iterabili permettono lo spacchettamento(unpacking),ovvero assegnare gli elementi della sequenza a delle label
# Il type str è un oggetto immutabile, non può essere riassegnato in questo modo:pippo[2] = 'l' 
# Il type liste e mutabile, il type tuple è immutabile

pippo = 'pippo'
# pippo[2] = 'l' non può essere eseguito,restituisce errore "TypeError: 'str' object does not support item assignment""
print (pippo[2] , type(pippo))
pippo = 'pluto'
print (pippo , type(pippo))

# eseguo lo spacchettamento
lettera0 , lettera1 , lettera2 = pippo[0:3]
print (lettera0 , lettera1 , lettera2)

# dichiaro una lista e ne modifico un elemento
lista = [2 , 5 , 12]
print (type(lista))
print (lista)
lista[0] = 4
print (lista)
print (lista.__len__())

# dichiaro una tuple
tupla = ('a' , 'b' , 'a' , 'c' , 'o')
print (type(tupla))
print (tupla)
# tupla[0] = 'b' non può essere eseguito,restituisce errore "TypeError: 'tuple' object does not support item assignment"