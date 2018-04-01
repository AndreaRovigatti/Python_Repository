#!/usr/bin/python
# -*- coding: utf-8 -*
# l'introspezione è la capacità di ottenere informazioni sugli oggetti:
#     la classe built-in type indica la classe di un oggetto
#     la funzione built-in id() indica l'identità di un oggetto  
#     la funzione built-in dir() serve per elencare alcuni attributi dell'oggetto in questione
#     la funzione built-in hasattr() serve per verificare se un oggetto ha un determinato attributo
#     la funzione built-in help() serve per reperire le informazioni dalle docstring su un determinato data core type/funzione,la funzione deve essere
#     la funzione built-in isinstance() dice se un oggetto appartiene a una classe\data core type o meno
#     la funzione built-in callable() dice se un oggetto è chiamabile,quindi se esegue del codice al suo interno   
# scritta senza parentesi,altrimenti analizza il risultato della funzione
# una stringa ad inizio funzione\metodo,meglio se racchiusa fra """ , è una docstring e viene assegnata all attributo __doc__
# attraverso help(funzione o metodo) si richiama la docstring in testa, che viene memorizzata in __doc__
def funzComplex():
    """funzione di prova"""
    return 1+2j
help(funzComplex)    
#print(funzComplex.__doc__) da bash funziona,qui no