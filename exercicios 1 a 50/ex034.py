salario = float(input("Informe o salário do colaborador: R$"))
if salario <= 1250:
    print(f"O novo salário é de R${salario + (salario * (15/100))}")
else:
    print(f"O novo salário é de R${salario + (salario * (10/100))}")
