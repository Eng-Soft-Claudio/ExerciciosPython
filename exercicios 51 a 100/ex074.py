from random import randint
from time import sleep
print("-=" * 20)
print("  Gerando cinco números aleatórios...")
print("-=" * 20)
lista = []
for n in range (5):
    lista.append(randint(1, 100))
    sleep(1)
    print(lista[n], end=" ")
    print("...")
tupla = tuple(lista)
print("-=" * 20)
print(f"O maior número da tupla é: {max(tupla):5}")
print(f"O menor número da tupla é: {min(tupla):5}")
print("-=" * 20)