# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima os números 
# no intervalo entre 1 e 100. 
# Os números devem ser apresentados na horizontal.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)


class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
    
    def imprimir_numeros(self, inicio, fim):
        # este metodo vai ser sobrecarregado
        print()


class Listagem(Numeros):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def imprimir_numeros(self):
        for numero in range(self.inicio, self.fim):
            print(numero, end=' ')


contagem = Listagem(1, 101)
contagem.imprimir_numeros()