# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Evolua o programa anterior para um código que pergunte 
# ao usuário qual o intervalo que ele deseja ver  impresso.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO B')
print('-' * 20)

# Entrada
inicio = int(input('Entre com o 1° número do seu intervalo: '))
fim = int(input('Entre com o ultimo número do seu intervalo: '))

# Processamento
for c in range(inicio,fim):
    print('----')
    print(f'{c}')

# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)
