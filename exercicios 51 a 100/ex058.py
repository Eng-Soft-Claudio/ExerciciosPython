from random import randint

print("===  JOGO DA ADIVINHAÇÃO  ===")
print("Tente acertar o número aleatório entre 1 e 10")
palpite = 0
numero_pc = randint(1, 10)
numero_pj = int(input("Insira um número entre 1 e 10: "))
while numero_pj not in range(1, 11):
    print("Número inválido! Escolha novamente...")
    numero_pj = int(input("Insira um número entre 1 e 10: "))
while numero_pj != numero_pc:
    if numero_pj < numero_pc:
        palpite += 1
        print("Mais!! Tente outra vez!")
        numero_pj = int(input("Qual seu palpite?  "))
        if numero_pj not in range(1, 11):
            print("Número inválido! Escolha novamente...")
            numero_pj = int(input("Qual seu palpite?  "))
    if numero_pj > numero_pc:
        palpite += 1
        print("Menos!! Tente outra vez!")
        numero_pj = int(input("Qual seu palpite? "))
        while numero_pj not in range(1, 11):
            print("Número inválido! Escolha novamente...")
            numero_pj = int(input("Qual seu palpite? "))
    if numero_pj == numero_pc:
        palpite += 1
        print(f"Parabéns!!\nAcertou com {palpite} palpites.")
        exit()

