#!/usr/bin/python
# -*- coding: utf-8 -*
# In Python non ci sono le variabili classiche , ma istanze di oggetti derivate dai Data Core Type generici:
#      numeri   :int , bool , complex , float
#      insiemi  :set
#      sequenze :str, byte , list , tuple
#      dizionari:dict
# Ogni oggetto ha
#      tipo         type(oggetto)    
#      identità     id(oggetto)          
#      attributi    oggetto.attributo
#                   oggetto.attributo() -->Funzione 
#                   se l'attributo può essere chiamato con () alla fine allora è callable, quindi permette di eseguire un blocco di istruzioni, e nell'ambito delle istanze 
#                   dei Core Data Type è una funzione(vedi sotto per più informazioni).
#                   Gli attributi che iniziano e finiscono con __ sono attributi speciali o magici
# NB:classe ed oggetto sono entità distinte!               
tot = 0 
for i in range(5):   # ciclo va da 0 a 4  
    tot +=i
print (tot , "fuori dal ciclo")
print (type(tot))
stringa = "ciao a tutti"
print (type(stringa))
print (55+22 , (55+22).bit_length())
# dir(oggetto) restituisce una lista dei nomi degli attributi piu' significativi di un oggetto
print (dir(stringa))
print (dir(tot)) 
print (sum)
# callable(oggetto.attributo) restitusce true o false se l'attributo e' callable o meno
# callable significa che è possibile chiamare l'identificativo(attributo) con () ed eventuale argomento, e quindi permette di eseguire un blocco di codice
# un identificativo callable di un oggetto derivato dal Core Data Type è una funzione; per quanto concerne le classi si parlerà di metodi che sono della stessa
# categoria delle funzioni.
print (callable(stringa.__len__))
if (stringa.__len__):
    print (stringa.__len__())
# hasattr(istanza , 'attributo') restituisce true/false a seconda che l'oggetto abbia o meno l'attributo del secondo argomento       
print (hasattr(stringa , '__coerce__'))
print (hasattr(tot , '__coerce__'))  
# il testo spezzato in pù linee si delinea con ''' """ 
stringaPiuLinee = '''questa stringa è spalmata
due 
tre
quattro
cinque righe'''
print (stringaPiuLinee)