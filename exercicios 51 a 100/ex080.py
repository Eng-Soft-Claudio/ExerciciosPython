print("*" * 40)
print(f'{"CINCO VALORES NUMÉRICOS":^40}')
print("*" * 40)

lista = []

for contador in range ( 0 , 5):
    numero = int(input("Digite um valor: "))
    if contador == 0 or numero > lista[-1]:
        lista.append(numero)
        print("Adicionado ao final da lista...")
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f"Adicionado na posição {posicao} da lista...")
                break
            posicao += 1
print("*" * 40)
print(f"Os valores digitados foram: {lista}")