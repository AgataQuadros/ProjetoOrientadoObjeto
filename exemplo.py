def calcular_desconto(preco, cliente):
    if cliente.vip():
        if preco > 100:
            return preco * 0.90
        else:
            return preco * 0.95
        
    else:
        return preco