import pandas as pd
import numpy as np

data = pd.read_csv('raw.csv', error_bad_lines=False, sep=';')
# data = pd.read_csv('test.csv', sep=';')
# df1 = pd.read_csv("http://pythonhow.com/wp-content/uploads/2016/01/Income_data.csv")

for col in data.columns:
    print data[col]

SIRENS = data['SIREN'].str.decode('iso-8859-1').str.encode('utf-8')
NICS = data['NIC'].str.decode('iso-8859-1').str.encode('utf-8')
BIZNAME = data['L1_NORMALISEE'].str.decode('iso-8859-1').str.encode('utf-8')
ZIPS = data['CODPOS'].str.decode('iso-8859-1').str.encode('utf-8')
ACTIVITIES = data['LIBAPET'].str.decode('iso-8859-1').str.encode('utf-8')



data2 = pd.DataFrame(SIRENS, columns=['SIREN'])
data2['NICS'] = NICS
data2['BIZNAME'] = BIZNAME
data2['ZIPS'] = ZIPS
data2['ACTIVITIES'] = ACTIVITIES

data2 = data2.sort_values('ACTIVITIES')


## data2.to_csv('out.csv', sep=';', encoding='utf-8')
## data2.to_csv('out.csv', sep=';', encoding='latin-1')

writer = pd.ExcelWriter('out.xlsx')
data2.to_excel(writer, 'Sheet1')
writer.save()

