import time
print("Vamos criar um triângulo")
lado = 0
triangulo = []
while not lado == 3:
     triangulo.append(int(input("Informe um segmento de reta: ")))
     lado += 1
time.sleep(1)
print("Analisando...")
time.sleep(1)
print("...")
time.sleep(1)
if triangulo[0] + triangulo[1] > triangulo[2] and triangulo[1] + triangulo[2] > triangulo[0] and triangulo[0] + triangulo[2] > triangulo[1]:
    print("Os segmentos de reta podem formar um triângulo.")
    pass
else:
    print("Os segmentos de reta não podem formar um triângulo.")
    exit()
time.sleep(1)
print("...")
time.sleep(1)
print("Analisando...")
time.sleep(1)
print("...")
if triangulo[0] == triangulo[1] == triangulo[2]:
    forma = "EQUILÁTERO"
elif triangulo[0] != triangulo[1] != triangulo[2] != triangulo[0]:
    forma = "ESCALENO"
else:
    forma = "ISÓSCELES"
time.sleep(1)
print(f"Os segmentos de reta formam um triângulo {forma}")