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


# Classe
class Frase:
    def __init__(self, frase):
        self.frase = frase

    def imprimir_frase(self, frase):
        pass


class TesteLooping(Frase): # nome de classe composto não separa
    def __init__(self, frase):
        self.frase = frase

    def imprimir_frase(self):
        while (True):
            frase2 = input('Digite F para sair do Loop!!! : ')

            if 'f' not in frase2:
                print('')
                print('Digite f...')
            else:
                print('-' * 20)
                print('Fim do Loop!!Muito Obrigado!!')
                break


# Processamento
loop = TesteLooping('Eu estou em looping!!')
loop.imprimir_frase()


# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)