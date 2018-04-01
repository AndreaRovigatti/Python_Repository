#!/usr/bin/python
# -*- coding: utf-8 -*
from datetime import datetime

# attraverso class si può creare una classe\type generico e successivamente delle istanze relative al class\type(ricalca il meccanismo dei Core Data Type)
# La funzione speciale __init__() viene richiamata automaticamente quando si istanzia un oggetto relativo alla classe indicata, facendo riferimento all'istanza 
# appena creata(vedi argomento self) ed agli argomenti passati alla definizione dell'istanza(Pippo e FooSurname verranno passati a nome e cognome di __init__)
# I metodi della classe vengono definiti da def nomeMetodo(self , [argomento/i]): dentro il blocco class , quindi a livello di __init__

class Persona:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
        self.iscrizione = datetime.now()
    def concatena(self):
        return self.nome + self.cognome
    def verificaNome(self , nomeVerifica):
        if self.nome == nomeVerifica:
            return True
        else:
            return False               

p1 = Persona("Pippo", "FooSurname")
print p1.nome , p1.cognome , p1.iscrizione , p1.concatena() , p1.verificaNome("cane")        
