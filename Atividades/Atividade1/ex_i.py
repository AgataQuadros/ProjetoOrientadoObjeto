# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que receba um valor em reais, 
# depois calcule quantos dólares daria para comprar com esse valor.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO I')
print('-' * 20)

# iniciando classe
class Convercao:
    def __init__(self, real):
        self.real = real
    
    def dolares(self):
        dolar = real / 5
        return dolar

# Entrada
real = (float(input('Digite o valor em real: ')))

resultado = Convercao(real)
dolar = resultado.dolares()

# Saída
print('')
print('-' * 20)
print(f'Se você tem R${real} então você pode ter ${dolar}')
print('-' * 20)
print('')
print('=' * 50)