# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Agata Quadros (Gaia)
# Data 02/09/2024
# Objetivo: Faça um programa que peça 4 notas, 
# após a entrada de dados calcular a média das notas digitadas.

# Biblioteca
import os

# Limpando o terminal
os.system('cls')

print('=' * 50)
print('EXERCÍCIO C')
print('-' * 20)

# Criando a classe
class Turma:
    def __init__(self, nota1 , nota2 , nota3 , nota4):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def media_nota(media):
        media = (nota1 + nota2 + nota3 + nota4) / 4
        return media


# Entrada
nota1 = float(input('Lançe a 1ª nota: '))
nota2 = float(input('Lançe a ª nota: '))
nota3 = float(input('Lançe a ª nota: '))
nota4 = float(input('Lançe a 4ª nota: '))

notas = Turma(nota1, nota2, nota3, nota4)
media = notas.media_nota()

# Saida
print('Média')
print('')
print(f'A média dessa turma é: {media}')
print('')
print('=' * 50)