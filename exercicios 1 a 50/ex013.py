salario_antigo = float(input("Informe o salário do colaborador: R$"))
aumento = 15/100
salario_novo = salario_antigo + (salario_antigo * aumento)
print(f"O colaborador com o salário de R${salario_antigo:.2f}, com um aumento de 15%, terá um novo salário de R${salario_novo:.2f}")