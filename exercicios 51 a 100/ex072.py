numero = int(input("Informe um número entre 0 e 20: "))
tupla = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "CATORZE", "QUINZE", "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")
continua = "S"
while True:
    if numero not in range (0, 21):
        print("Número inválido, tente novamente...")
        numero = int(input("Informe um número entre 0 e 20: "))
    else:
        print(f"Você digitou o número {tupla[numero]}")
        break
