def calcular_juros(valor, taxa, meses):
    return valor * (1 + taxa/100) ** meses

valor = float(input("Valor: R$ "))
taxa = float(input("Taxa % ao mês: "))
meses = int(input("Meses: "))
print(f"Total com juros: R$ {calcular_juros(valor, taxa, meses):.2f}")