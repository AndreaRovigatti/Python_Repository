#!/usr/bin/python
# -*- coding: utf-8 -*
# La libreria standard di Python è strutturata in moduli, si importano attraverso
# import modulo
# oppure
# from modulo import attributo1, attributo2, ..., attributon
# cambia come si referenziano gli attributi/funzioni all'interno del codice
# vedi http://docs.python.org/3/library/index.html
import math
from datetime import datetime
from sys import platform, version_info , version
import os

print (math.pi)
print (datetime.now())
print (platform)
print (os.environ.__len__())
u = os.uname()
print (u)
print (version_info)
print (version)

# il sistema esegue python2.7 per default,capire come impostare il 3
# https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3
# nota 9/10 giugno 2017
# ho impostatao python3 dai settaggi(settings.json)