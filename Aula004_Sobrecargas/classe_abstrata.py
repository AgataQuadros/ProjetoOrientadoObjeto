import os
from abc import ABC, abstractmethod

# Classe abstrata
class MetodoDePagamento(ABC):

    @abstractmethod
    def procesar_pagamento(self, valor):
        # Processa um pagamento qualquer
        pass

# Subclasse concreta
class CartaoDeCredito(MetodoDePagamento):

    def procesar_pagamento(self, valor):
        print('Pagamento cam cartão de crédito.')
        print(f'Valor pago: R${valor}')

# Subclasse concreta
class Boleto(MetodoDePagamento):

    def procesar_pagamento(self, valor):
        print('Emissão de boleto.')
        print(f'Pagagamento de R${valor}')


os.system('cls')
#intanciando as classes filhas
pagamento_cartao = CartaoDeCredito()
pagamento_cartao.procesar_pagamento(5000.00)

pagamento_boleto = Boleto()
pagamento_boleto.procesar_pagamento(500.00)