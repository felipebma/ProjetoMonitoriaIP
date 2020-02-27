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

# Gráfico pizza sobre as potências dos motores
    
    
