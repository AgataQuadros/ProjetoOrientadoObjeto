import os


class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

# Solicitando entrada de dados de usuario
os.system('cls')
print('-' * 70)
marca = input('Qual a marca do veículo? ')
modelo = input('Qual o modelo do veículo? ')
ano = int(input('Qual o ano do veículo? '))
cor = input('Qual a cor do veículo? ')

# Criando um objeto da classe Veiculo com os dados fornecidos pelo usuario
veiculo1 = Veiculo(marca, modelo, ano, cor)

print('-' * 70)
print('\n Informações da Pessoa:')
print('=' * 70)
print(f'Marca: {veiculo1.marca}')
print(f'Modelo: {veiculo1.modelo}')
print(f'Ano: {veiculo1.ano}')
print(f'Cor: {veiculo1.cor}')
print('-' * 70)