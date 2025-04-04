cidade = str(input("Informe o nome de uma cidade: ")).strip().upper()
santo = cidade.split()
if santo[0] == "SANTO":
    print("A cidade informada começa com o nome SANTO.")
else:
    print("A cidade informada não começa com SANTO.")