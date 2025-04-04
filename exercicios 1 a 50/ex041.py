import datetime
print("~" * 38)
print("|  CONFEDERAÇÃO NACIONAL DE NATAÇÃO  |")
print("~" * 38)
print("~" * 38)
print("|  CATEGORIAS DE ATLETAS POR IDADE   |")
print("~" * 38)
ano_atual = datetime.date.today().year
ano_nascimento = int(input("| Ano de nascimento do atleta: "))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print("Categoria: MIRIM")
elif idade <= 14:
    print("Categoria: INFANTIL")
elif idade <= 19:
    print("Categoria: JUNIOR")
elif idade <= 25:
    print("Categoria: SÊNIOR")
else:
    print("Categoria: MASTER")
