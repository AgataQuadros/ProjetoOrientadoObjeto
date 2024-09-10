# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que imprima
# os números primos entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO F')
print('-' * 20)


# Criando classes
class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def numeros_primos(self, inicio, fim):
        # este metodo vai ser sobrecarregado
        pass


class Primos(Numeros):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def numeros_primos(self):
        for numero in range(self.inicio, self.fim):
            for primo in range(self.inicio, numero):
                if numero % primo == 0:
                    break
            else:
                print(numero, end=' ')


# Processamento
intervalo = Primos(2, 100)
intervalo.numeros_primos()

# Saida
print()
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)
