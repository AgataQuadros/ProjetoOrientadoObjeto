from math import pi

# Define a classe base Forma com um metodo area
# que não faz nada (é quase uma classe abstrata)


class Forma:
    def area(self):
        pass


# Define a classe Circulo que herda de Forma 
# O construtor __init__ inicializa o atributo raio
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    # Define o metodo area para calcular a area do
    # circulo usando a formula π * raio²
    def area(self):
        return pi * (self.raio ** 2)
    

# Define a classe Retangulo que herda de Forma
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Define o metodo ara para calcular a area
    # do retangulo usando a formla largura * atura
    def area(self):
        return self.largura * self. altura
    

# Define a classe Quadrado que herda Retangulo
class Quadrado(Retangulo):
    def __init__(self, lado):
        super.__init__(lado, lado)


# Define uma função exibir_area que aceita um
# objeto forma e imprime sua area
# O metodo area é chamado no objeto forma
def exibir_area(forma):
    print(f'A area da forma é: {forma.area()}')


# Criando instancias e Circulo, Retangulo e Quadrado
circulo = Circulo(5)
retangulo = Retangulo(4, 6)
quadrado = Quadrado(3)

# Chama a função exibir_area para cada instância
# o metodo area apropriado é chamado para 
# cada objeto, mostrando polimorfismo
exibir_area(circulo)
exibir_area(retangulo)
exibir_area(quadrado)