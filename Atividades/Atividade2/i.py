# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um algoritmo que imprima a frase 
# "estou em looping" e, em seguida, solicite 
# ao usuário digitar uma letra. Caso a letra seja o 
# “f" finalize a aplicação. Do contrário, 
# imprima novamente a mesma frase até que
# o caractere “f" seja digitado.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO I')
print('-' * 20)

# Entrada
print('Eu estou em loop!')
print('')

# Processamento
while (True):
    frase2 = input('Digite F para sair do Loop!!! : ')

    if 'f' not in frase2:
        print('')
        print('Digite f...')
    else:
        print('-' * 20)
        print('Fim do Loop!!Muito Obrigado!!')
        break

# Saída
print('')
print('-' * 20)
print('=' * 50)