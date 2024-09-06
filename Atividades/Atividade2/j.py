# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Crie um programa que realiza a 
# contagem de 1 até 100, usando apenas de 
# números ímpares, ao final do processo exiba 
# na tela quantos números ímpares foram 
# encontrados nesse intervalo, 
# assim como a soma dos mesmos.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO J')
print('-' * 20)

# Entrada
quantidade_impar = 0
soma = 0

# Processamento
for c in range(0,100):
    if not c % 2 == 0:
        quantidade_impar += 1
        soma += c
        print(c, end=' - ')

print()
print('----')
print(quantidade_impar)
print('----')
print(soma)

# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)