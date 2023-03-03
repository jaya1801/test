#pip install openpyxl or tablib[xlsx]
#pip install tablib
import tablib

data = tablib.Dataset()
import_file = 'jsondatafile.json'
data.json = '[' + str(open(import_file, 'r').read()) + ']'

with open('file.xlsx', 'wb') as f:
    f.write(data.export('xlsx'))
f.close()
