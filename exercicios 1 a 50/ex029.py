import random
velocidade = random.randint(20, 200)
print(f"A velocidade registrada foi de {velocidade} km/h.")
radar = (velocidade - 80) * 7
if velocidade > 80:
    print(f"Foi registrada uma multa no valor de R${radar:.2f}")
else:
    pass