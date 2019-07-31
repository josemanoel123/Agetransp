import os
import pandas as pd
path = 'C:/Users/jjunior/Documents'

os.chdir(path)
arq ='acidentes trechos ROTA116.xlsx'
a=pd.read_excel(arq,sheet_name = 'Planilha3')


teste = []
for i in a['SEGMENTOS']:
    teste.append(float(i[11:13]+'.'+i[14:]))
a.insert(2, "Trecho", teste , True)
