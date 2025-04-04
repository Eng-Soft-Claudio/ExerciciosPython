valor_normal = float(input("Informe o valor do produto: R$"))
print("Código de Operação")
print("1 -- À vista (Dinheiro/Pix)")
print("2 -- À vista (Cartão Débito)")
print("3 -- Parcelado (2 x no Cartão Crédito)")
print("4 -- Parcelado (3x no Cartão Crédito)")
print("5 -- Parcelado (4x ou mais no Cartão Crédito)")
condicao_pagamento = int(input("Informe o código da operação: "))
if condicao_pagamento == 1:
    valor_final = valor_normal - (valor_normal * (10 / 100))
    print(f"O valor final do produto será: R${valor_final:.2f}")
elif condicao_pagamento == 2:
    valor_final = valor_normal
    print(f"O valor final do produto será: R${valor_final:.2f}")
elif condicao_pagamento == 3:
    valor_final = valor_normal + (valor_normal * (5 / 100))
    print(
        f"O valor final do produto será de: R${valor_final:.2f}\nDividido em 2 parcelas iguais de R${(valor_final/2):.2f}"
    )
elif condicao_pagamento == 4:
    valor_final = valor_normal + (valor_normal * (10 / 100))
    print(
        f"O valor final do produto será de: R${valor_final:.2f}\nDividido em parcelas iguais de R${(valor_final / 3):.2f}"
    )
elif condicao_pagamento == 5:
    valor_final = valor_normal + (valor_normal * (20 / 100))
    parcelas = int(input("Informe o número de parcelas: "))
    print(
        f"O valor final do produto será de: R${valor_final:.2f}\nDividido em {parcelas} parcelas iguais de R${(valor_final/parcelas):.2f}"
    )
else:
    print("Código de Operação Inválido\nReinicie a Operação de Venda")
    exit()
