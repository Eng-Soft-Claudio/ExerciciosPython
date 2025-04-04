from random import randint
from time import sleep

print("-=" * 20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-=" * 20)

contador = 0

while True:
    numero = int(input("Diga um valor: "))
    palpite = str(input("Par ou Ímpar [P/I]: ")).upper().strip()[0]
    computador = randint(1, 10)
    soma = numero + computador

    if soma % 2 == 0:
        resultado = "DEU PAR"
    else:
        resultado = "DEU ÍMPAR"

    print("--" * 20)
    print(
        f"Você jogou {numero} e o computador {computador}.\nTotal de {soma} {resultado}"
    )
    print("--" * 20)

    if soma % 2 == 0 and palpite == "P":
        print("Você VENCEU!\nVamos jogar novamente...")
        print("-=" * 20)
        contador += 1
    if soma % 2 != 0 and palpite == "I":
        print("Você VENCEU!\nVamos jogar novamente...")
        print("-=" * 20)
        contador += 1
    if soma % 2 == 0 and palpite == "I":
        print("Você PERDEU!")
        print("-=" * 20)
        print(f"GAME OVER! Você venceu {contador} vezes.")
        break
    if soma % 2 != 0 and palpite == "P":
        print("Você PERDEU!")
        print("-=" * 20)
        print(f"GAME OVER! Você venceu {contador} vezes.")
        break
