# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que converta metros 
# em centímetros e milímetros.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

# Iniciando Classe
class Converter:
    def __init__(self, metros):
        self.metros = metros
    
    def centimetos(self):
        centimetros = metros * 100
        return centimetros
    
    def milimetros(self):
        milimetros = metros * 1000
        return milimetros

# Entrada
metros = float(input('Digite o metro: '))

resultado = Converter(metros)
centimetros = resultado.centimetos()
milimetros = resultado.milimetros()

# Saida
print('')
print('-' * 20)
print(f'A converção dos metros {metros} para centímetros é {centimetros} cm')
print(f'A converção dos metros {metros} para milímetros é {milimetros} mm')
print('-' * 20)
print('')
print('=' * 50)