total = 0
caro = 0
contador = 0
produto_barato = ""

while True:
    
    nome = str(input("Nome do produto: ")).upper().strip()
    valor = float(input("Valor do produto R$"))
    total += valor
    contador += 1

    if valor > 1000:
        caro += 1
    
    if contador == 1:
        menor = valor
    else:
        if valor < menor:
            menor = valor
            produto_barato = nome
    
    # Loop
    continua = str(input("Nova venda [S/N]: ")).upper().strip()[0]
    if continua == "S":
        print("Continuando...")
        pass
    else:
        print("Encerrando...")
        print(f"Número de produtos acima de R$1000,00: {caro}")
        print(f"Nome do mais barato: {produto_barato}")
        print(f"Valor total da compra: R${total:.2f}")
        break