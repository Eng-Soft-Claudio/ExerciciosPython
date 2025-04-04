numero = int(input("Informe um número inteiro: "))
total = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print("\033[33m", end="")
        total += 1
    else:
        print("\033[31m", end="")
    print(f"{c}", end=" ")
print(f"\nO número {numero} é divisível por {total} números.")
if total == 2:
    print("É um número primo.")
else:
    print("Não é um número primo.")
