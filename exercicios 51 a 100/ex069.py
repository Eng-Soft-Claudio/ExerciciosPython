contador = 0
homem = 0
mulher = 0
maior = 0

while True:
    contador += 1
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    idade = int(input("Idade: "))
    print("-" * 20)
    if idade > 18: 
        maior += 1
    if sexo == "M":
        homem += 1
    if sexo == "F" and idade < 20:
        mulher += 1
    continua = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if continua == "S":
        pass
    else:
        print(f"Pessoas com mais de 18 anos: {maior}")
        print(f"Homens cadastrados: {homem}")
        print(f"Mulher com menos de 20 anos: {mulher}")
        break
    
    