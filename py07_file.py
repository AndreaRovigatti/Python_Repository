#!/usr/bin/python
# -*- coding: utf-8 -*

# open() crea una istanza dell'oggetto file object che permette di interagire con un file presente nel file system(detto file sottostante)
#
# apertura file:per default lettura, se dobbiamo scrivere indicare 'w' come secondo argomento
f = open('/home/andrea/wrkspaceJs/forEach.js')
print (f.name)
#read() restituisce il contenuto del file in una stringa
print(f.read()) 

# un ciclo for su un file permette di leggere un file riga per riga
for recordFile in open('/home/andrea/wrkspaceJs/forEach.js'):
    print(recordFile)

# apro un file in scrittura ed eseguo la write
fWrite = open('pippo' , 'w')
fWrite.write('stringa di provaaaaaaaaaaaaaaaaaa')    