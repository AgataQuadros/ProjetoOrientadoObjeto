# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa 
# com entrada de dados para calcular o perímetro de um retângulo.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO J')
print('-' * 20)

# Criando classe
class Retangulo:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    
    def calcular(self):
        resolver = (lado1 * 2) + (lado2 * 2)
        return resolver


# Etrada
lado1 = (float(input('Entre com o lado 1: ')))
lado2 = (float(input('Entre com o lado 2: ')))

conta = Retangulo(lado1, lado2)
resultado = conta.calcular()

# Saída
print('')
print('-' * 20)
print(f'O perímetro do retangulo é {resultado}')
print('-' * 20)
print('')
print('=' * 50)