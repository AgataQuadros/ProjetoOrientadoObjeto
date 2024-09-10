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


# Criando classes
class Numeros:
    def __init__(self, inicio, fim, exclui1, exclui2, exclui3):
        self.inicio = inicio
        self.fim = fim
        self.exclui1 = exclui1
        self.exclui2 = exclui2
        self.exclui3 = exclui3

    def excluir_nemeros(self, inicio, fim,  exclui1, exclui2, exclui3):
        # este metodo vai ser sobrecarregado
        pass


class Excluindo(Numeros):
    def __init__(self, inicio, fim, exclui1, exclui2, exclui3):
        self.inicio = inicio
        self.fim = fim
        self.exclui1 = exclui1
        self.exclui2 = exclui2
        self.exclui3 = exclui3

    def excluir_nemeros(self):
        for numero in range((inicio),(fim+1)):
            if numero == exclui1 or numero == exclui2 or numero == exclui3:
                continue
            print(numero, end=" ")


# etrada
inicio = int(input('Entre com o inicio do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))
print('Aqui você escolherá 3 numeros para excluir da sequencia')
exclui1 = int(input('Entre com o 1º número: '))
exclui2 = int(input('Entre com o 2º número: '))
exclui3 = int(input('Entre com o 3º número: '))

# Processamento
intervalo = Excluindo(inicio, fim, exclui1, exclui2, exclui3)
intervalo.excluir_nemeros()

# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)