continuar = "S"
soma = 0
contador = 0
maior = 0
menor = 0
while continuar == "S":
    numero = int(input("Informe um número: "))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input("Deseja continuar (S/N)? ")).upper().strip()[0]
    if continuar == "N":
        print("Este programa será encerrado...")
        media = soma / contador
        print(f"Foram informados {contador} números.\nA soma deles é {soma} e a média deles é {media}.\nO maior número informado foi {maior} e o menor número informado foi {menor}.")
        exit()
    else:
        print("O programa continua sua execução...")


