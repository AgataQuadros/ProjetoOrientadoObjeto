# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que receba 
# um número qualquer e calcule o dobro e o triplo desse número.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO F')
print('-' * 20)

# Iniciando classe
class Dub_trip:
    def __init__(self, numero):
        self.numero = numero
    
    def triplo(self):
        triplo = numero * 3
        return triplo
    
    def dobro(self):
        dobro = numero * 2
        return dobro



# Entrada
numero = (float(input('Digite o numero: ')))

resultado = Dub_trip(numero)
dobro = resultado.dobro()
triplo = resultado.triplo()

# Saída
print('-' * 20)
print('')
print(f'O drobro de {numero} é {dobro}')
print(f'enquanto seu tríplo é {triplo}')
print('')
print('=' * 50)