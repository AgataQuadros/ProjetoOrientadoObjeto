# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que receba um número inteiro, 
# depois imprima sua tabuada de multiplicação.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO H')
print('-' * 20)

class Tabuada:
    def __init__(self, numero):
        self.numero = numero

    def multiplica(self):
        m1 = numero * 1
        m2 = numero * 2
        m3 = numero * 3
        m4 = numero * 4
        m5 = numero * 5
        m6 = numero * 6
        m7 = numero * 7
        m8 = numero * 8
        m9 = numero * 9
        m10 = numero * 10

        return m1 , m2 ,m3 ,m4, m5 , m6 , m7 , m8 , m9 , m10


# Entrada
numero = (int(input('Qual número que você quer multiplicar?')))

resultado = Tabuada(numero)
tabuada = resultado.multiplica()

# Saida 
print('')
print('-' * 20)
print(f'Os resultados da tabua de {numero} é, respectivamente: {tabuada} ')
print('-' * 20)
print('')
print('=' * 50)