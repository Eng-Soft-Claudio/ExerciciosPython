soma_pares = 0
soma_coluna = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("Informe um valor: "))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
print("=-" * 30)
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f"[{matriz[linha][coluna]:^7}] ", end="")
    print()
print("=-" * 30)
soma_coluna = matriz[0][2] + matriz[1][2]+ matriz[2][2]
print(f"A soma dos valores pares é {soma_pares}")
print(f"A soma dos valores da terceira coluna é {soma_coluna}")
print(f"o maior valor da segunda linha é {max(matriz[1])}")