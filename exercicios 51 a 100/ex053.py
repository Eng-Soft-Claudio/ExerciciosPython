import unidecode
frase = str(input("Digite uma frase: ")).upper().strip()
frase = unidecode.unidecode(frase)
lista = frase.split()
junto = "".join(lista)
junto = junto.replace(",","").replace(".","")
inverso = junto[::-1]
if inverso == junto:
    print("A frase digitada é um palíndromo.")
else:
    print("A frase digitada não é um palíndromo")
print(f"Frase tratada: {junto}\nFrase inversa: {inverso}")

