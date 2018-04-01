#!/usr/bin/python
# -*- coding: utf-8 -*
#insieme è rappresentato dal type set , è un contenitore non ordinato, mutabile negli elementi ma immutabile nel numero totale degli elementi
#è possibile eseguire le operazioni fra più insiemi
insieme1 = {1 , 2 , 3 , 4 , 5 , 8}
insieme2 = {5 , 8 , 12 , 16}
print (type(insieme1))

print ("unione      :" , insieme1 | insieme2)
print ("Intersezione:" , insieme1 & insieme2)
print ("1 - 2       :" , insieme1 - insieme2)
print ("2 - 1       :" , insieme2 - insieme1)

#dizionario è rappresentato dal type dict , è un contenitore mutabile non ordinato, che rappresenta delle coppie chiave/valore
#Non vi si accede per indice ma per chiave
dizionario = {'chiave1':1 , 'chiave8':8 , 'chiave5':5.88 , 4:"ciao"}
print (type(dizionario))
print (dizionario)
print (dizionario[4])
print ("chiave12" in dizionario)