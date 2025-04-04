altura = float(input("Informe a altura do paciente: "))
peso = float(input("Informe o peso do paciente: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"Seu IMC é de: {imc:.1f}\nCaracterizado como ABAIXO DO PESO")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é de: {imc:.1f}\nCaracterizado como PESO IDEAL")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é de: {imc:.1f}\nCaracterizado como SOBREPESO")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é de: {imc:.1f}\nCaracterizado como OBESIDADE")
else:
    print(f"Seu IMC é de: {imc:.1f}\nCaracterizado como OBESIDADE MÓRBIDA")