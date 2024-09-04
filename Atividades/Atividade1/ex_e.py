# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que receba um número inteiro 
# e mostre o sucessor e antecessor.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)

# Iniciando a classe
class Ante_Sucess:
    def __init__(self, numero):
        self.numero = numero
    
    def antecessor(self):
        antecessor = self.numero - 1
        return antecessor

    def sucessor(self):
        sucessor = self.numero + 1
        return sucessor

# Entrada
numero = int(input('Entre com um numero inteiro: '))
resultado = Ante_Sucess(numero)
antecessor = resultado.antecessor()
sucessor = resultado.sucessor()

# Saida
print('')
print('-' * 20)
print(f'O sucessor do numero {numero} é {sucessor}')
print(f'O antecessor do numero {numero} é {antecessor}')
print('-' * 20)
print('')
print('=' * 50)