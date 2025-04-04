lista = [[], []]
lista_par = []
lista_impar = []

for r in range (0, 7):
    numero = (int(input("Informe um valor: ")))
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
lista[0].append(lista_par)
lista[1].append(lista_impar)

print(lista)