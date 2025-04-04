preco_produto = float(input("Informe o valor do produto: R$"))
desconto = 5/100
preco_desconto = preco_produto - (preco_produto * desconto)
print(f"Valor do produto: R${preco_produto:.2f}")
print(f"Valor com 5% de desconto: R${preco_desconto:.2f}")