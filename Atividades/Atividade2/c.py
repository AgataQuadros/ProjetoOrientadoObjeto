# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima os números 
# no intervalo entre 1 e 10 em ordem inversa.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)


# Criando as classes
class Numeros:
    def __init__(self, inicio, meio, fim):
        self.inicio = inicio
        self.meio = meio
        self.fim = fim
    
    def imprimir_sequencia(self, inicio, meio, fim):
        # este metodo vai ser sobrecarregado
        print()


class Sequencia(Numeros):
    def __init__(self, inicio, meio, fim):
        self.inicio = inicio
        self.meio = meio
        self.fim = fim
    
    def imprimir_sequencia(self):
        for numero in range(self.inicio, self.meio, self.fim):
            print(numero, end=' ')


# Processamento]
sequencia_numeros = Sequencia(10, 0, -1)
sequencia_numeros.imprimir_sequencia()

# Saida
print()
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)