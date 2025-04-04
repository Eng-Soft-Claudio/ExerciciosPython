print("=x=" * 15)
print("Informe três segmentos de reta para analisar\n     se elas podem formar um triângulo.")
print("=x=" * 15)
segmento_a = int(input("Informe o primeiro segmento de reta: "))
segmento_b = int(input("Informe o segundo segmento de reta: "))
segmento_c = int(input("Informe o terceiro segmento de reta: "))
print("=x=" * 16)
if segmento_a + segmento_b > segmento_c and segmento_a + segmento_c > segmento_b and segmento_b + segmento_c > segmento_a:
    print("Os segmentos podem formar um triangulo.")
else:
    print("Os segmentos não podem formar um triângulo.")
print("=x=" * 16)
