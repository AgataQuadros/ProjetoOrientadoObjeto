# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que peça 3 valores ,
# depois calcule e imprima  a soma e a multiplicação desses valores.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO A')
print('-' * 20)


# Criando a Classe Soma
class Calculos:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Metodo Somar
    def somar(self):
        resultado = self.a + self.b + self.c
        return resultado
    
    # Metodo Multiplicar
    def multiplicar(self):
        resultado = self.a * self.b * self.c
        return resultado

# Entrada
os.system('cls')
print('-' * 20)
a = int(input('Entre com o 1º valor: '))
b = int(input('Entre com o 2º valor: '))
c = int(input('Entre com o 3º valor: '))

# Objeto da classe
valores = Calculos(a, b, c)

resultado_soma = valores.somar()
resultado_produto = valores.multiplicar()

# Saida
print('-' * 20)
print(f'A soma dos valores propostos é: {resultado_soma}')
print(f'O produto dos valores propostos é: {resultado_produto}')
print('=' * 50)