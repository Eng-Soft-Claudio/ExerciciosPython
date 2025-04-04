print("=x=" * 16)
valor_casa = float(input("Informe o valor da casa: R$"))
valor_salario = float(input("Informe o valor do salário: R$"))
qtde_anos_pgto = int(input("Informe a quantidade de anos para pagamento: "))
print("=x=" * 16)
valor_prestacao = valor_casa / (qtde_anos_pgto * 12)
percentual_aprovacao = valor_salario * (30 / 100)
if valor_prestacao < percentual_aprovacao:
    print("O financiamento habitacional foi aprovado.")
else:
    print("O financiamento habitacional foi reprovado.")
print("=x=" * 16)
print(f"O financiamento habitacional no valor de:\n"
      f"R${valor_casa:.2f}\n"
      f"Dividido em parcelas iguais de:\n"
      f"R${valor_prestacao:.2f}\n"
      f"Por um período de {qtde_anos_pgto * 12} meses")
print("=x=" * 16)
