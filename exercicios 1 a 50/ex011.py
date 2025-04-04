largura = float(input("Informe a largura da parede (metros): "))
altura = float(input("Informe a altura da parede (metros): "))
area = largura * altura
tinta = area / 2
print(f"A parede informada possui {largura:.2f} metros de largura, {altura:.2f} metros de altura, e {area:.2f}m² de área.")
print(f"Serão necessários {tinta:.2f} litros de tinta")