# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que some a quantidade 
# de números pares encontrados no intervalo entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)

# Entrada
quantidade_pares = 0
soma = 0


# Processamento
for c in range(0, 102):
    if c % 2 ==0:
        quantidade_pares += 1
        soma += c
        
print('----')
print(quantidade_pares)
print(soma)

# Saida
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)