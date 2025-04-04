print("=x=" * 16)
print("Conversor de números")
print("=x=" * 16)
print("Digite 1 para binário...\nDigite 2 para octal...\nDigite 3 para hexadecimal...")
base = int(input("Informe a base de conversão: "))
while base < 1 or base > 3:
    print("Escolha inválida...")
    base = int(input("Informe a base de conversão: "))
print("=x=" * 16)
numero = int(input("Informe um número inteiro a ser convertido: "))
print("=x=" * 16)
if base == 1:
    print(f"O número {numero} convertido em BINARIO é: {bin(numero)}")
elif base == 2:
    print(f"O número {numero} convertido para OCTAL é: {oct(numero)}")
elif base == 3:
    print(f"O número {numero} convertido em HEXADECIMAL é: {hex(numero)}")
print("=x=" * 16)