# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Crie um programa que realiza a 
# contagem de 1 até 100, usando apenas de 
# números ímpares, ao final do processo exiba 
# na tela quantos números ímpares foram 
# encontrados nesse intervalo, 
# assim como a soma dos mesmos.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO J')
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
        quantidade_impares = 0
        soma = 0

        for numero in range(self.inicio, self.fim):
            if not numero % 2 == 0:
                quantidade_impares += 1
                soma += numero
        print(quantidade_impares)
        print(soma)


# Processamento
intervalo = Sequencia(0, 100)
intervalo.quantidade_numeros()


# Saida
print('')
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)