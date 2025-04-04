sexo = str(input("Informe o sexo (M/F): ")).upper().strip()[0]
while sexo not in "MF":
    sexo = str(input("Dados inválidos. Informe o sexo (M/F): ")).upper().strip()[0]
    
print(f"O sexo informado foi: {sexo}")
    