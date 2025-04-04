contador = 0
soma = 0
while True:
    numero = int(input("Informe um número ou digite 999 para parar: "))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f"Número de números informados: {contador}\nSoma desses números: {soma}")
