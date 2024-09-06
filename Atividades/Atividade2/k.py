# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Crie um programa que pede que o usuário 
# digite um nome ou uma frase, verifique se esse 
# conteúdo digitado é um palíndromo ou não, 
# exibindo em tela esse resultado.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO K')
print('-' * 20)

# Entarda de dados.
while True:
    print('-'*79)
    frase = input('Digite a frase que deseja verificar: ')
    print('-'*79)
    # Validação de dados.
    if (frase.isnumeric()):
        print('Entrada inválida!')
    else:
        break

# Processameento de dados.
sem_espaço = frase.replace(' ', '').lower()
invertida = sem_espaço[::-1]
if (sem_espaço == invertida):
    resposta = f'{frase} é um palíndromo!'
else:
    resposta = f'{frase} não é um palíndromo!'

# Saída de dados.
print('='*79)
print(resposta)
print('='*79)

# Imprimindo título de fim.
print('.'*79)
print('Fim do programa! Obrigado!')
print('.'*79)