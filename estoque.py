estoque = 50

def vender(qtd):
    global estoque
    if qtd <= estoque:
        estoque -= qtd
        print(f"Vendido! Restam {estoque} no estoque")
    else:
        print(f"Estoque insuficiente! Só tem {estoque}")

qtd = int(input("Quanto quer vender? "))
vender(qtd)