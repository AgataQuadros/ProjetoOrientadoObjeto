import csv
import os


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta

# Fução para obter dados do usuario e criar a instancia conta bancaria
def obter_dados_conta():
    numero_conta = input('Qual o numero da conta? ')
    nome_titular = input('Qual o nome do titular? ')
    saldo = float(input('Qual o saldo inicial? '))
    agencia = input('Qual a agência? ')
    tipo_conta = input('Qual o tipo de conta? ')
    return ContaBancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)


# Lista para armazenar contAS BANCARIAS
contas = []

# Obter dados das contas
while True:
    conta = obter_dados_conta()
    contas.append({
        'numero_conta': conta.numero_conta,
        'nome_titular': conta.nome_titular,
        'saldo': conta.saldo,
        'agencia': conta.agencia,
        'tipo_conta': conta.tipo_conta})
    
    continuar = input('Deseja adicionar outra conta? (s/n): ')
    if continuar.lower() != 's':
        break

# Caminho para a onde o arquivo CSV sera salvo
pasta = 'arquivos_csv/conta/'

# Verificando se a pasta existe, se não, irá cria-la
os.makedirs(pasta, exist_ok=True)

# Nome para o arquivo csv para gravar as informações
arquivo = 'arquivos_csv/conta/conta.csv'

# Escreve a lista de dicionários no arquivo csv
with open(arquivo, mode='w', newline='') as conta:
    fieldnames = ['numero_conta', 'nome_titular', 
                  'saldo', 'agencia', 'tipo_conta']
    writer = csv.DictWriter(conta, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    for registro in contas:
        writer.writerow(registro)

print(f'As informações da conta foram salvas em {arquivo}')