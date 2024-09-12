class ClassePai: # Super Classe
    # Metodo construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Metodo que sera sobrecarregado
    def metodo_classe(self):
        print('Aqui vou multiplicar a e b!')
        resultado = self.a * self.b
        print('Este cálculo esta sendo realizado')
        print('pelo método da classe pai!')
        print(f'O resultado da multiplicação de {self.a} e {self.b} é {resultado}')


class ClasseFilha(ClassePai):
    # Metodo construtor
    def __init__(self, a, b):
        super().__init__(a, b) # Chama o construtor da classe pai
        # Não é necessario redefinir a variavel self.a e self.b,
        # pois ja foram inicializadas palo construtor pai

    # Sobrecarga de metodo
    def metodo_classe(self):
        # Primeiro, executa o metodo da classe pai
        super().metodo_classe()
        # Depois, executa o metodo da classe filha
        resultado = self.a * self.b
        print(f'O resultado da soma na classe filha é: {resultado}')


# Programa principal
teste = ClasseFilha(1, 2)
teste.metodo_classe()