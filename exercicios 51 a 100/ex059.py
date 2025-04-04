print("=-=" * 10)
print("    OPERAÇOES ARITMÉTICAS")
print("=-=" * 10)
numero_1 = int(input("Informe um número: "))
numero_2 = int(input("Informe outro número: "))
escolha = 0
print("=-=" * 10)
print(
    "Selecione:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa"
)
while escolha != 5:
    escolha = int(input("Informe sua opção: "))
    if escolha not in range(1, 6):
        print("Opção inválida! Informe uma opção...")
        escolha = int(input("Informe sua opção: "))
    if escolha == 1:
        print(f"A soma entre {numero_1} e {numero_2} é: {numero_1 + numero_2}")
    if escolha == 2:
        print(f"A multiplicação entre {numero_1} e {numero_2} é: {numero_1 * numero_2}")
    if escolha == 3:
        if numero_1 > numero_2:
            print(f"O maior número digitado foi: {numero_1}")
        else:
            print(f"O maior número digitado foi: {numero_2}")
    if escolha == 4:
        numero_1 = int(input("Informe um novo número: "))
        numero_2 = int(input("Informe outro novo número: "))
    if escolha == 5:
        print("Encerrando o programa...")
        print("=-=" * 10)
        exit()
    print("=-=" * 10)
