# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima os números pares entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)

for c in range(0,100):
    if c % 2 == 0:
        print('----')
        print(c)

 
# Saida
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)