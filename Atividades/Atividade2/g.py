# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 06/09/2024
# Objetivo: Faça um programa que calcule 
# os números primos em um intervalo 
# pré-determinado pelo usuário.

# Biblioteca
import os


# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO G')
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
         if inicio < 2:
            print(f'Não existe numero primo de {inicio}, tente outro numero')
         else:
            for numero in range(self.inicio, self.fim):
                  for primo in range(self.inicio, numero):
                     if numero % primo == 0:
                        break
                  else:
                     print(numero, end=' ')



# Entrada
inicio = int(input('Entre com o inicio do intervalo: '))
fim = int(input('Entre com o final do intervalo: '))

# Processamento
intervalo = Primos(inicio, fim)
intervalo.numeros_primos()

# Saida
print()
print('-' * 20)
print('Fim do exercício :D')
print('=' * 50)