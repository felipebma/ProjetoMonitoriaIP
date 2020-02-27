import re

class Automovel:
    def __init__(self, info = {}):
        self.categoria = info['categoria'] if 'categoria' in info else 'Não Informada'
        self.modelo = info['modelo'].title() if 'modelo' in info else 'Não Informado'
        self.tipo = info['tipo de veículo'] if 'tipo de veículo' in info else 'Não Informado'
        self.marca = info['marca'].title() if 'marca' in info else self.modelo.split()[0].title()
        if self.marca == 'Gm - Chevrolet':
            self.marca = 'Chevrolet'
        self.cidade = info['cidade'] if 'cidade' in info else 'Não Informada'
        self.ano = info['ano'].replace(' ','') if 'ano' in info else 'Não Informado'
        self.km = int(info['quilometragem']) if 'quilometragem' in info else 'Não Informado'
        self.cor = info['cor'] if 'cor' in info else 'Não Informada'
        self.n_portas = info['portas'].split()[0] if 'portas' in info else 'Não Informado'
        self.conservacao = info['conservação'] if 'conservação' in info else 'Não Informada'
        self.combustivel = info['combustível'] if 'combustível' in info else 'Não Informado'
        self.final_da_placa = info['final de placa'] if 'final de placa' in info else 'Não Informado'
        self.motor = float(info['potência do motor']) if 'potência do motor' in info else 'Não Informado'
        if self.motor=='Não Informado':
            motor = re.search('[0-9].[0-9]',self.modelo)
            if motor is not None:
                self.motor = float(motor[0])
        self.transmissao = info['câmbio'] if 'câmbio' in info else 'Não Informada'
        self.n_fotos = info['fotos'] if 'fotos' in info else 'Não Informado'
        self.concessionaria = info['concessionaria'] if 'concessionaria' in info else 'Não Informada'
        self.preço = info['preço'] if 'preço' in info else 'Não Informado'

    def getInfo(self):
        return {
            'Categoria':self.categoria,
            'Modelo':self.modelo,
            'Tipo':self.tipo,
            'Marca':self.marca,
            'Cidade':self.cidade,
            'Ano':self.ano,
            'Quilometragem':self.km,
            'Cor':self.cor,
            'Nº de Portas': self.n_portas,
            'Conservação':self.conservacao,
            'Combustível':self.combustivel,
            'Final da Placa':self.final_da_placa,
            'Potência do Motor':self.motor,
            'Câmbio':self.transmissao,
            'Nº de fotos':self.n_fotos,
            'Concessionária':self.concessionaria,
            'Preço':self.preço
        }
    