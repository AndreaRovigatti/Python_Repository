#!/usr/bin/python
# -*- coding: utf-8 -*
# le istruzioni sopra vanno sempre in testa e servono per abilitare il charset Unicode invece dell'Asci:
#     in questo modo posso usare è/à/ò/ù nei commenti ;)
# --------------------   
# --Pythonic Way    --
# --------------------
# Dovrebbe esserci un solo modo di sviluppare ed organizzare codice in Python,ovvero la Pythonic Way
# --------------------   
# --Blocco di codice--
# --------------------
# Un blocco di codice nidificato(if , ciclo , classe) viene aperto da istruzione + : ed è composto da istruzioni a seguire 
# tutte identate allo stesso modo, la PEP-0008 consiglia di mettere 4 spazi per identare ogni blocco.
# Esempio
# istruzione inizio blocco01:
#     istruzione 01 blocco01
#     istruzione 02 blocco01
#     .....
#     istruzione  n blocco01
# 1234 
# --------------------
# --Istruzioni      --
# --------------------
# le istruzioni non sono delimitate da caratteri, basta andare su una nuova linea
# eventualmente si possono mettere più istruzioni sulla stessa linea separandole da ; ma è meglio evitare nei file .py
# Invece può essere utile separare le istruzioni con ; se si lanciano comandi python da stringa di comando,esempio:
# python - c "a = 'python';print a;"
#
print ("istruzione")
for i in range(4):
    print ("sono dentro al ciclo for istruzione 1")
    if i % 2 == 0:
        print (i , "è un numero pari")    # separando con la virgola viene aggiunto uno spazio fra le istanze stampate
    else:
        print (i , "è un numero dispari")