n1 = int(input("Informe um número inteiro: "))
n2 = int(input("Informe um número inteiro: "))
n3 = int(input("Informe um número inteiro: "))
n4 = int(input("Informe um número inteiro: "))
n5 = int(input("Informe um número inteiro: "))
n6 = int(input("Informe um número inteiro: "))
soma = 0
if n1 % 2 == 0:
    soma += n1
if n2 % 2 == 0:
    soma += n2
if n3 % 2 == 0:
    soma += n3
if n4 % 2 == 0:
    soma += n4
if n5 % 2 == 0:
    soma += n5
if n6 % 2 == 0:
    soma += n6
if soma != 0:
    if n1 % 2 == 0 or n2 % 2 == 0 or n3 % 2 == 0 or n4 % 2 == 0 or n5 % 2 == 0 or n6 % 2 == 0:
        print(
            f"Os números informados foram:\n"
            f"{n1} | {n2} | {n3} | {n4} | {n5} | {n6}\n"
            f"A soma dos números pares é: {soma}"
        )
elif soma == 0:
    print("Não havia números pares informados.")
else:
    print("Não havia números pares informados.")
