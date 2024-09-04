# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que receba e divida 2 números. 
# A saída da divisão precisará ser formatada com 4 casas decimais.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

# Criando classe
class Divisao:
    def __init__(self, ):
        print
# Entrada
dividendo = (float(input('Entre com o divendendo: ')))
divisor = (float(input('Entre com o divisor: ')))

# Processamento
resultado = dividendo / divisor

# Saída
print('')
print('-' * 20)
print(f'O resultado da divisão entre {dividendo} / {divisor} é {resultado: .4f}')
print('-' * 20)
print('')
print('=' * 50)