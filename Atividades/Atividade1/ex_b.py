# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que peça o ano do 
# seu nascimento e calcule a sua idade.

# Biblioteca
import os
from datetime import datetime

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
print('-' * 20)

# Processamento

# Iniciando a classe
class Aniversario:
    def __init__(self, data_nascimento):
        self.data_nascimento = data_nascimento
    
    def data_nascimento_usuario(self, data_nascimento):
        hoje = datetime.now()
        nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        
        idade = hoje.year - nascimento.year - \
            ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        
        return idade

# Entrada
nascimento = input('Digite a data do seu aniversario (dd/mm/aaaa): ')
aniversario = Aniversario(nascimento)
idade = aniversario.data_nascimento_usuario(nascimento)

# Saida
print('-' * 20)
print('')
print(f'Ora, se você nasceu em {nascimento} então você tem {idade} anos!')
print('')
print('=' * 50)
