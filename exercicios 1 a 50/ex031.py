distancia = float(input("Informe a distância da viagem em Quilômetros: "))
if distancia <= 200:
    valor = distancia * 0.5
else:
    valor = distancia * 0.45
print(f"O valor da passagem é R${valor:.2f}")