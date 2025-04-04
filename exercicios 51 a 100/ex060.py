from math import factorial
numero = int(input("Informe um número inteiro: "))
fatorial = factorial(numero)
print(f"{numero}! = ", end="")
while numero > 0:
    print(f"{numero}", end="")
    print(f" x " if numero > 1 else " = ", end="")
    numero -= 1
print(f"{fatorial}")