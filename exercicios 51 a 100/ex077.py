palavras = (
    "casa",
    "homem",
    "flor",
    "amor",
    "livro",
    "cidade",
    "carro",
    "animal",
    "papel",
    "computador",
    "feliz",
    "grande",
    "verde",
    "claro",
    "escuro"
)

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper():>12}  contém as letras: ", end='')
    for letra in palavra:
        if letra.upper() in "AEIOU":
            print(f"{letra.upper()}", end=" ")