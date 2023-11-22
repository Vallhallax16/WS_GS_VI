#Importe de clases hechas
import GetLinks
import Scholar
import HTML_Table_S
from HTML_Table_GS import HTML_Table_GS
import HTML_Table_RG
#Fin del importe de clases

import csv
from html import escape
import re
"""
#Inicializacion de clase Table_GS
table_gs = HTML_Table_GS()

googleScholarContent = table_gs.htmlTableGS()

with open('index.html','r',encoding='utf-8') as content_file:
    content = content_file.read()

temp = re.sub('<!--START HERE GS-->.*?<!--END HERE GS-->',googleScholarContent,content, flags=re.DOTALL)
f = open('index.html','wb')
f.write(temp.encode('utf-8'))
"""


#----------------------------------------------------------------------------------------------------------------
#scorpusContent = htmlTableS()

#with open('index.html','r',encoding='utf-8') as content_file:
#    content = content_file.read()

#temp = re.sub('<!--START HERE S-->.*?<!--END HERE S-->',scorpusContent,content, flags=re.DOTALL)
#f = open('index.html','wb')
#f.write(temp.encode('utf-8'))

#----------------------------------------------------------------------------------------------------------------
#researchGateContent = htmlTableRG()

#with open('index.html','r',encoding='utf-8') as content_file:
#    content = content_file.read()

#temp = re.sub('<!--START HERE RG-->.*?<!--END HERE RG-->',researchGateContent,content, flags=re.DOTALL)
#f = open('index.html','wb')
#f.write(temp.encode('utf-8'))