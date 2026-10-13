def calcular_comissao(vendas):
    if vendas <= 1000:
        return vendas * 0.05
    elif vendas <= 5000:
        return vendas * 0.10
    else:
        return vendas * 0.15

vendas = float(input("Valor vendido: R$ "))
print(f"Comissão: R$ {calcular_comissao(vendas):.2f}")