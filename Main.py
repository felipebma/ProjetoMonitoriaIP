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
        motor_frequency['{0}'.format(motor)]+=1
    else:
        motor_frequency['{0}'.format(motor)]=1
motorFreqData = {'motor':[],'Frequência':[]}
for motor in motor_frequency:
    motorFreqData['motor'].append(motor)
    motorFreqData['Frequência'].append(motor_frequency[motor])
motorDF = pd.DataFrame({'Frequência':motorFreqData['Frequência']},
                            index=motorFreqData['motor'])
motorDF.plot(kind='pie',y='Frequência', title='Potência do Motor')
plt.show()
    
    

