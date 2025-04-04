peso = []
for p in range(1, 6):
    peso.append(float(input(f"Informe o peso da {p}ª pessoa: ")))
print(
    f"O maior peso registrado foi de {max(peso):.2f} kg e o menor peso registrado foi de {min(peso):.2f} kg"
)
