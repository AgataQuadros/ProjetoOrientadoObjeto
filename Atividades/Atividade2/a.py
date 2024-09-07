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
    
    def contagem(self):
        lista = []
        for i in range(self.inicio, self.fim):
            lista.append(i)
            return f'{lista}'
            

    
class Imprimir(Numeros):
    def contagem():
        Imprimir()

lista_numero = Numeros(1,100)
print(lista_numero.contagem())