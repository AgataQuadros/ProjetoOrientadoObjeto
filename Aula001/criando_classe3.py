import os


class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo, agencia, tipo_conta):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo
        self.agencia = agencia
        self.tipo_conta = tipo_conta

print('-' * 70)
os.system('cls')
numero_conta = input('Qual o numero da conta? ')
nome_titular = input('Qual o nome do titular? ')
saldo = input('Qual o saldo inicial? ')
agencia = input('Qual a agência? ')
tipo_conta = input('Qual o tipo de conta? ')

# Criando um objeto da classe ContaBancaria com os dados fornecidos pelo usuario
conta = ContaBancaria(numero_conta, nome_titular, saldo, agencia, tipo_conta)

# Acessando e imprimindo atributos do objeto
print('-' * 70)
print('\n Informações da Pessoa:')
print('=' * 70)
print(f'Numero daconta:')
print(f'Nome do titular: ')
print(f'Saldo: ')
print(f'Agência: ')
print(f'Tipo de conta: ')
print('-' * 70)