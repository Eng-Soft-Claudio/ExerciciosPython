termo = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
decimo = termo + 10 * razao
for s in range(termo, decimo, razao):
    print(s, end=", ")