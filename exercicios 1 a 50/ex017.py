import math
print("="*50)
cateto_op = float(input("Informe o comprimento do cateto oposto: "))
cateto_ad = float(input("Informe o comprimento do cateto adjacente:"))
print("="*50)
hipotenusa = math.hypot(cateto_op, cateto_ad)
print(f"A hipotenusa deste triângulo é: {hipotenusa}")