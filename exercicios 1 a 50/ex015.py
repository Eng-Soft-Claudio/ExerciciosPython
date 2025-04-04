print("="*50)
print(" "*15,"LOCADORA DE VEÍCULOS")
print("="*50)
km = float(input("Informe a quantidade de km percorrido: "))
dias = int(input("Informe a quantidade de dias utilizados:"))
valor_km = km * 0.15
valor_dias = dias * 60
valor_total = valor_km + valor_dias
print("="*50)
print(f"O veículo foi locado por:\n{km:.2f} km percorridos\n{dias} dias de locação\nValor total da locação:\nR${valor_total:.2f}")
print("="*50)