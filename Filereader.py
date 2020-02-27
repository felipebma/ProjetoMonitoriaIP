import os
import re
from Automovel import Automovel

def readFile(file):
    data = file.readlines()
    info = {}    
    if(data[0].strip()=='Categoria'):
        info['categoria'] = data[1].strip()
        for i in range(2,len(data)-1,2):
            info[data[i].strip().lower()] = data[i+1].strip()
    else:
        info['modelo'] = data[0].strip()
        info['cidade'] = data[1].strip()
        text = ''
        for l in data:
            text += l
        ano = re.search('ANO\n[0-9/\s]*',text)
        if ano is not None:
            info['ano'] = ano[0].strip().split('\n')[1]
        km = re.search('KM\n[0-9]*',text)
        if km is not None:
            info['quilometragem'] = int(km[0].split('\n')[1])
        cor = re.search('COR\n[a-zA-Z]*', text)
        if cor is not None:
            info['cor'] = cor[0].split('\n')[1]
        portas = re.search('PORTAS\n[0-9]*',text)
        if portas is not None:
            info['portas'] = portas[0].split('\n')[1]
        preço = re.search('R. [0-9,\.]*',text)
        if preço is not None:
            info['preço'] = preço[0]
        conservação = re.search('Conservação: [a-zA-Z]*',text)
        if conservação is not None:
            info['conservação'] = conservação[0].split()[1]
        combustível = re.search('Combustível: [a-zA-Z]*',text)
        if combustível is not None:
            info['combustível'] = combustível[0].split()[1]
        placa = re.search('placa: [0-9]*',text)
        if placa is not None:
            info['final de placa'] = placa[0].split()[1]
        motor = re.search('Motor: [0-9\.]*',text)
        if motor is not None:
            info['potência do motor'] = motor[0].split()[1]
        transmissão = re.search('Transmissão: [a-zA-Zá]*',text)
        if transmissão is not None:
            info['câmbio'] = transmissão[0].split()[1]
        fotos = re.search('[0-9]* fotos',text)
        if fotos is not None:
            info['fotos'] = fotos[0].split()[0]
        concessionaria = re.search('fotos\n[^\n]*',text)
        if concessionaria is not None:
            info['concessionaria'] = concessionaria[0].split('\n')[1]
        
    return Automovel(info)