primeiro = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        contador += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão Aritmética finalizada com {total} termos.")