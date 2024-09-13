class ClassePai:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class ClasseFilha(ClassePai):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def soma(self):
        soma = self.a + self.b
        print(f'A soma é {soma}')

conta = ClasseFilha(1, 2)
conta.soma()