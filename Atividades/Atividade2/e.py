# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que some a quantidade
# de números pares encontrados no intervalo entre 0 e 100.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO E')
print('-' * 20)


# Criando as Classes
class Numeros:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def quantidade_numeros(self, inicio, fim):
        # este metodo vai ser sobrecarregado
        pass


class Sequencia(Numeros):
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

    def quantidade_numeros(self):
        quantidade_pares = 0
        somatorio = 0

        for numero in range(self.inicio, self.fim):
            if numero % 2 == 0:
                quantidade_pares += 1
                somatorio += numero
        print(quantidade_pares)
        print(somatorio)


# Processamento
intervalo = Sequencia(0, 101)
intervalo.quantidade_numeros()


# Saida
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)
