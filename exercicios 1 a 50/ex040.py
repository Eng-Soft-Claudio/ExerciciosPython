nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))
media = (nota_1 + nota_2) / 2
if media < 5:
    print(f"A média do aluno foi {media:.2f}. Situação: REPROVADO")
elif media >= 5 and media < 7:
    print(f"A média do aluno foi {media:.2f}. Situação: RECUPERAÇÃO")
else:
    print(f"A média do aluno foi {media:.2f}. Situação: APROVADO")