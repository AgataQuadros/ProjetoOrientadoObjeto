import os


class Pessoa:
    def __init__(self, nome, cpf, nascimento, cep, cidade, estado):
        # Iniciando atributos
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

# Solicitando entrada de dados de usuario
os.system('cls')
print('-' * 70)
nome = input('Qual o seu nome? ')
cpf = input('Qual o seu cpf? ')
nascimento = input('Qual o seu ano de nascimento? ')
cep = input('Qual o seu cep? ')
cidade = input('Qual o seu cidade? ')
estado = input('Qual o seu estado? ')

# Criando um objeto da classe Pessoa com os dados fornecidos palo usuário
pessoa1 = Pessoa(nome, cpf, nascimento, cep, cidade, estado)

# Acessando e imprimindo atributos do objeto
print('-' * 70)
print('\n Informações da Pessoa:')
print('=' * 70)
print(f'Nome: {pessoa1.nome}')
print(f'CPF: {pessoa1.cpf}')
print(f'Ano de Nascimento: {pessoa1.nascimento}')
print(f'CEP: {pessoa1.cep}')
print(f'Cidade: {pessoa1.cidade}')
print(f'Estado: {pessoa1.estado}')
print('-' * 70)