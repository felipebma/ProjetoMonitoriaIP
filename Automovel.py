import re

class Automovel:

    def __getMarca(self, info):
        marca = info['marca'].title() if 'marca' in info else self.__modelo.split()[0].title()
        if marca == 'Gm - Chevrolet':
            marca = 'Chevrolet' 
        return marca

    def __getMotor(self,info):
        motor = float(info['potência do motor']) if 'potência do motor' in info else 'Não Informado'
        if motor=='Não Informado':
            motor = re.search('[0-9].[0-9]',self.__modelo)
            if motor is not None:
                motor = float(motor[0])
        return motor

    def __init__(self, info = {}):
        self.__categoria = info['categoria'] if 'categoria' in info else 'Não Informada'
        self.__modelo = info['modelo'].title() if 'modelo' in info else 'Não Informado'
        self.__tipo = info['tipo de veículo'] if 'tipo de veículo' in info else 'Não Informado'
        self.__marca = self.__getMarca(info)
        self.__cidade = info['cidade'] if 'cidade' in info else 'Não Informada'
        self.__ano = info['ano'].replace(' ','') if 'ano' in info else 'Não Informado'
        self.__km = int(info['quilometragem']) if 'quilometragem' in info else 'Não Informado'
        self.__cor = info['cor'] if 'cor' in info else 'Não Informada'
        self.__n_portas = info['portas'].split()[0] if 'portas' in info else 'Não Informado'
        self.__conservacao = info['conservação'] if 'conservação' in info else 'Não Informada'
        self.__combustivel = info['combustível'] if 'combustível' in info else 'Não Informado'
        self.__final_da_placa = info['final de placa'] if 'final de placa' in info else 'Não Informado'
        self.__motor = self.__getMotor(info)
        self.__transmissao = info['câmbio'] if 'câmbio' in info else 'Não Informada'
        self.__n_fotos = info['fotos'] if 'fotos' in info else 'Não Informado'
        self.__concessionaria = info['concessionaria'] if 'concessionaria' in info else 'Não Informada'
        self.__preço = info['preço'] if 'preço' in info else 'Não Informado'

    def getInfo(self):
        return {
            'Categoria':self.__categoria,
            'Modelo':self.__modelo,
            'Tipo':self.__tipo,
            'Marca':self.__marca,
            'Cidade':self.__cidade,
            'Ano':self.__ano,
            'Quilometragem':self.__km,
            'Cor':self.__cor,
            'Nº de Portas': self.__n_portas,
            'Conservação':self.__conservacao,
            'Combustível':self.__combustivel,
            'Final da Placa':self.__final_da_placa,
            'Potência do Motor':self.__motor,
            'Câmbio':self.__transmissao,
            'Nº de fotos':self.__n_fotos,
            'Concessionária':self.__concessionaria,
            'Preço':self.__preço
        }
    