import os
import re
import pandas as pd
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
from Automovel import Automovel
import Filereader


with os.scandir('./inputs') as entries:
    autos = []
    for entry in entries:
        with open(entry,'r') as f:
            auto = Filereader.readFile(f)
            autos.append(auto)
    data = {}
    for key in autos[0].getInfo():
        data[key] = []
    for auto in autos:
        info = auto.getInfo();
        for key in info:
            data[key].append(info[key])

dataframe = pd.DataFrame(data)


dataframe = dataframe.sort_values(by=['Potência do Motor'])
#Criando gráfico pizza da potência do Motor
dataframe['Potência do Motor'].value_counts().plot(kind='pie', title='Número de Carros por Potência do Motor', legend=True, figsize=(10,10), autopct='%1.0f%%')
plt.savefig('./Gráficos/Pizza(Potência do Motor).png')
plt.close()

#Line de número de carros por marca
dataframe['Marca'].value_counts().plot(kind='line', title='Número de Carros por Marca', legend=True, figsize=(10,10))
plt.savefig('./Gráficos/Line(Carros por Marca).png')
plt.close()


dataframe = dataframe.sort_values(by=['Ano'])
#Gráfico de Barra de preferência de cor através dos anos
dataframe.groupby(['Ano','Cor']).size().unstack().plot(kind='bar',stacked=True, title='Preferência de Cor Através dos Anos', color=['blue', 'white', 'silver', 'black'], edgecolor='black', figsize=(10,10))
plt.savefig('./Gráficos/Barra(Cor através dos Anos).png')
plt.close()

#Scatter de Câmbio por Marca
dataframe.plot(kind='scatter',x='Marca',y='Câmbio',title='Tipo de Câmbio Usado pelas Marcas', legend=True, figsize=(10,10))
plt.savefig('./Gráficos/Scatter(Câmbio por marca).png')
plt.close()
