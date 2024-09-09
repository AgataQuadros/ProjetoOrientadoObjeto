# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que verifique
# se o usuário e senha estão inseridos em 
# um banco de dados (fake). O usuário só terá 
# acesso se digitar os dados corretos 
# e, assim, sair do laço.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO L')
print('-' * 20)

# Banco de dados
usuario_bd = 'aluno'
senha_bd = '123@456'

usuario = str(input('Entre com o usuario: '))
senha = str(input('Entre com a senha: '))

#Processamento
while(True):
    if usuario != usuario_bd or senha != senha_bd:
        print('Usuario invalido!')
        usuario = str(input('Entre com o usuario: ')).lower()
        senha = str(input('Entre com a senha: '))
    else:
        break
print('logado...')

# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)
print()