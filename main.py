# Desafio 1 - Comissão
def calcular_comissao(vendas):
    if vendas <= 1000:
        return vendas * 0.05
    elif vendas <= 5000:
        return vendas * 0.10
    else:
        return vendas * 0.15

# Teste
vendas = float(input("Valor vendido: R$ "))
print(f"Comissão: R$ {calcular_comissao(vendas):.2f}")

# Desafio 2 - Estoque com UUID
import uuid

estoque = {}

def adicionar_produto(nome, qtd):
    id_unico = str(uuid.uuid4())[:8]
    estoque[id_unico] = {"nome": nome, "qtd": qtd}
    print(f"Produto {nome} adicionado com ID {id_unico}")
    return id_unico

# Desafio 3 - Juros Compostos
def juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa/100) ** tempo
    return montante

capital = float(input("Capital inicial: "))
taxa = float(input("Taxa %: "))
tempo = int(input("Meses: "))
print(f"Montante final: R$ {juros_compostos(capital, taxa, tempo):.2f}")