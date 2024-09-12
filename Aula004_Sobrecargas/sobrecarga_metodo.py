# Sobrecarrega de  Metodos

class ClassePai: # Super Classe
    # Metodo construtor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Para sobrecarregar
    # Vai ser usada para somar 2 numeros
    def metodo_classe(self, a, b):
        pass


class Classefilha(ClassePai): # Classe Derivada
    # Metodo construtos
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Sobrecarga de metodo
    def metodo_classe(self):
        return self.a + self.b
    

# Programa principal
teste = Classefilha(1, 2)
soma = teste.metodo_classe()

print(soma)