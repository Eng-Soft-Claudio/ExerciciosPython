numero_1 = int(input("Informe um número inteiro aleatório: "))
numero_2 = int(input("Informe outro número inteiro aleatório: "))
if numero_1 > numero_2:
    print(f"O numero {numero_1} é maior que o número {numero_2}.")
elif numero_2 > numero_1:
    print(f"O número {numero_2} é maior que o número {numero_1}.")
else:
    print("Os números são iguais.")