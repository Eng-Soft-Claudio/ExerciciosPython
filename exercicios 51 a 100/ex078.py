lista = []

for posição in range(0, 5):
    lista.append(int(input(f"Informe o número para a posição {posição}: ")))

maior = max(lista)
menor= min(lista)

print(f"O maior número informado foi: {maior}, nas posições: ", end="")
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f"{indice}... ", end=" ")

print(f"\nO menor número informado foi: {menor}, nas posições: ", end="")
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f"{indice}... ", end="")
