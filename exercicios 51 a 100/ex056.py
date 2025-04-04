soma_idades = 0
mulheres_abaixo_20 = 0
homem_velho = ""
idade_homem = 0
for i  in range (4):
    nome = str(input("Informe o nome da pessoa: ")).strip()
    idade = int((input("Informe a idade da pessoa: ")))
    sexo = str(input("Informe o sexo da pessoa: ")).strip().upper()
    soma_idades += idade
    if sexo == "F" and idade < 20:
        mulheres_abaixo_20 += 1
    if sexo == "M" and idade_homem < idade:
        homem_velho =  nome
        idade_homem = idade
if homem_velho == "":
    homem_velho = "Nenhum homem informado no grupo"
media_idades = soma_idades / 4
print(f"A média de idade do grupo de pessoas é {media_idades} anos.")
print(f"Nome do homem mais velho: {homem_velho}")
print(f"Número de mulheres abaixo de 20 anos no grupo: {mulheres_abaixo_20}")