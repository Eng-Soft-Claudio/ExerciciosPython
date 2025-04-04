flag = 0
contador = 0
soma = 0
while flag != 999:
    flag = int(input("Informe um número ou digite 999 para parar: "))
    if flag != 999:
        soma += flag
        contador += 1
print(f"Foram digitados {contador} números e a soma deles é: {soma}")