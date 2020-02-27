import os
import re
import pandas as pd
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



#Criando gráfico pizza da potência do Motor
motor_frequency = {}
for motor in dataframe['Potência do Motor']:
    if motor in motor_frequency:
        motor_frequency[motor]+=1
    else:
        motor_frequency[motor]=1

motorDF = pd.DataFrame({'Frequência':[*motor_frequency.values()]},
                            index=[*motor_frequency])
motorDF.plot(kind='pie',y='Frequência', title='Potência do Motor')
#plt.show()
plt.close()

#Line de número de carros por marca
marca_frequency = {}
for marca in dataframe['Marca']:
    if marca in marca_frequency:
        marca_frequency[marca]+=1
    else:
        marca_frequency[marca]=1
marcaDF = pd.DataFrame({'Marca':[*marca_frequency],'Número de Carros':[*marca_frequency.values()]})
marcaDF.plot.bar(x='Marca',y='Número de Carros', title='Número de Carros por Marca')
plt.show()
plt.close()


dataframe = dataframe.sort_values(by=['Ano'])
#Histograma de Câmbio por Ano

#Scatter de Cor por Ano
dataframe.plot(kind='scatter',x='Ano',y='Cor',title='Preferência de Cores Através dos Anos')
#plt.show()
plt.close()
