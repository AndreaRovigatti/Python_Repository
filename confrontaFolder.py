#!/usr/bin/python
# -*- coding: utf-8 -*
#codice scritto per girare su Python 2/Python 2.7
#https://docs.python.org/2/library/os.path.html
from sys import platform, version_info , version
import os , datetime , time
print ("Versione Python:", version)
print (" ")

class ScorriFileSystem:
    def __init__(self,indirizzo):
        #indirizzo da esaminare
        self.indirizzo = indirizzo
        #inizializzo lista con dizionario per ogni file letto
        self.listaIndirizzo = []
        #valuto se directory o file ed esamino di conseguenza
        if os.path.isdir(self.indirizzo):
            self.tipologia = 'dir'
            for elemIter in os.listdir(self.indirizzo):
                fullPath = self.indirizzo + elemIter
                if os.path.isfile(fullPath):
                    self.schedaFiles(fullPath)
        else:
            self.tipologia = 'file'
            self.schedaFiles(self.indirizzo)
    def schedaFiles(self,fullPath):
        fileFolder = open(fullPath)
        try:
            modTime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(os.path.getmtime(fullPath)))
        except OSError:
            modTime = "OSError!!"
        try:
            changeTime = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(os.path.getctime(fullPath)))
        except OSError:
            changeTime = "OSError!!"                
        dizionario = {"nomeFile":"" , "ultimaMod":"" , "directory":"" , "size":"" , "changeTime":""}    
        dizionario['directory'] = self.indirizzo
        dizionario['nomeFile'] = os.path.basename(fullPath)
        dizionario['ultimaMod'] = modTime
        dizionario['size'] = str(os.path.getsize(fullPath)) + " Bytes"
        dizionario['changeTime'] = changeTime
        self.aggiungiListaIndirizzo(dizionario)
    def aggiungiListaIndirizzo(self,dizionario):
        self.listaIndirizzo.append(dizionario)
    def stampaSituazione(self,fileStampa):
        f = open(fileStampa , 'w')
        for elemDict in self.listaIndirizzo:
            f.write(elemDict['directory'] + ';' + elemDict['nomeFile'] + ';' + elemDict['changeTime'] + ';' + elemDict['ultimaMod'] + ';' + elemDict['size'] + '\n')

print("Inizio")
folderA = ScorriFileSystem('/home/andrea/wrkspacePython/')
folderA.stampaSituazione("foooo.csv")
folderA = ScorriFileSystem('/home/andrea/wrkspaceJs/')
folderA.stampaSituazione("foooo.csv")
print("Fine")
