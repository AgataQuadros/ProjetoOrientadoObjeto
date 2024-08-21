import os


class Banco():
    def __init__(self, nome = '', agencia = 0, conta = 0, cpf =0, 
                 conta_corrente = 0,  poupanca = 0):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.cpf = cpf
        self.conta_corrente = conta_corrente
        self.poupanca = poupanca

    def deposito(self, valor):
        escolha = input('Conta corrente (cc)' 
                        'ou Poupança (po)? ').lower().strip()

        if escolha == 'cc':
            print(f'Valor do depósito: (+)R${valor}')
            print(f'Saldo anterior(cc): R${self.conta_corrente}')
            self.conta_corrente += valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('-' * 70)
        
        elif escolha == 'po':
            print(f'Valor do depósito: (+)R${valor}')
            print(f'Saldo anterior(po): R${self.poupanca}')
            self.poupanca += valor
            print(f'\tSaldo atual na Poupança: R${self.poupanca}')
            print('-' * 70)
        
        else:
            print('Opção invalida')

    def saque(self, valor):
        escolha = input('Conta corrente (cc) '
                        'ou Poupança (po)? ').lower().strip()
        
        if escolha == 'cc':
            print(f'Valor do saque: (+)R${valor}')
            print(f'Saldo anterior(cc): R${self.conta_corrente}')
            self.conta_corrente -= valor
            print(f'\tSaldo atual na Conta Corrente: R${self.conta_corrente}')
            print('-' * 70)
        
        elif escolha == 'po':
            print(f'Valor do saque: (+)R${valor}')
            print(f'Saldo anterior(po): R${self.poupanca}')
            self.poupanca -= valor
            print(f'\tSaldo atual na Poupança: R${self.poupanca}')
            print('-' * 70)
        
        else:
            print('Opção invalida')


os.system('cls')

# Coletar dados do usuario para criar uma nova conta
print('Preencha os dados para cria uma nova conta: ')
nome = input('Qual o seu nome? ')
agencia = int(input('Qual a sua agência? '))
conta = int(input('Qual a sua conta? '))
cpf = int(input('Qual o seu cpf? '))
conta_corrente = float(input('Qual a sua conta corrente? '))
poupanca = float(input('Qual a sua poupança? '))

# Criar um novo correntista
correntista = Banco(nome, agencia, conta, cpf, conta_corrente,  poupanca)


print('-' * 70)
print('Movimentação Bancária')
print('=' * 70)
opcao = input('Depósito ou Saque (D/S)? ').upper().strip()

if opcao == 'D':
    valor = float(input('Qual valor depositar? '))
    correntista.deposito(valor)

elif opcao == 'S':
    valor = float(input('Qual valor sacar? '))
    correntista.saque(valor)        
else:
    print('Opção invalida')  