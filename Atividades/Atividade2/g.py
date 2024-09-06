# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que calcule 
# os números primos em um intervalo 
# pré-determinado pelo usuário.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
print('-' * 20)

# Entrada
inicio = int(input('Entre com o inicio do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))

# Processamento
if inicio < 2:
   print(f'Não existe numero primo de {inicio}, tente outro numero')
else:
   for c in range((inicio),(fim)):
      for m in range(inicio,c):
         if c % m == 0:
            break
      else:
         print(c, end=' - ')