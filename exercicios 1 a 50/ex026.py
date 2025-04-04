frase = str(input("Digite uma frase qualquer: ")).upper()

if frase.find("A") is True:
    print(f"A letra 'A' aparece {frase.count("A")} vezes.")
    print(f"A primeira letra 'A aparece no índice {frase.find("A")}")
    print(f"A última letra 'A' aparece no índice {frase.rfind("A")}")
else:
    print("A frase informada não contém a letra 'A'.")
