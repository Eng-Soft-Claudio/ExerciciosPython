import math

print("=" * 50)
angulo = float(input("Informe um ângulo: "))
angulo = math.radians(angulo)
print("=" * 50)
print(f"Seno: {math.sin(angulo):.2f}")
print(f"Coseno: {math.cos(angulo):.2f}")
print(f"Tangente: {math.tan(angulo):.2f}")
print("=" * 50)
