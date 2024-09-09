# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima os números pares entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO D')
print('-' * 20)


# Criando as classes
class Sequencia:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
    
    def sequencia_pares(self, inicio, fim):
        # este metodo vai ser sobrecarregado
        print()


class Pares(Sequencia):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim
    
    def sequencia_pares(self):
        for numero in range(self.inicio, self.fim):
            if numero % 2 == 0:
                print(numero, end=' ')


# Processamento
numeros_pares = Pares(0, 100)
numeros_pares.sequencia_pares()
 
# Saida
print()
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)