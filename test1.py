#pip install openpyxl
#pip install tablib

import tablib
import json

data = tablib.Dataset()

temp = open('jsondatafile.json', 'r').read()

d = json.dumps(eval(temp)['Summary'])
data.json = '[' + d +']'

with open('file.xlsx', 'wb') as f:
    f.write(data.export('xlsx'))
f.close()
