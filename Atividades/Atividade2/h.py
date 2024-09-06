# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima 
# os valores no intervalo definidos pelo usuário.
# Defina 3 números que deverão ser ignorados, 
# ou seja, que não serão impressos na tela.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO H')
print('-' * 20)

# etrada
inicio = int(input('Entre com o inicio do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))
print('Aqui você escolherá 3 numeros para excluir da sequencia')
exclui1 = int(input('Entre com o 1º número: '))
exclui2 = int(input('Entre com o 2º número: '))
exclui3 = int(input('Entre com o 3º número: '))

# Peocessamento
for c in range((inicio),(fim)):
    if c == exclui1 or c == exclui2 or c == exclui3:
        continue
    print('')
    print(c)
    
# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)