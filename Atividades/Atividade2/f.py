# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima
# os números primos entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO F')
print('-' * 20)

# Processamento
for c in range(2,100):
    for m in range(2,c):
        if c % m == 0:
            break
    else:
        print('----')
        print(c)

# Saida
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)