import random
import time

print("=" * 30)
print("Adivinhe o número aleatório entre 0 e 5: ")
numero = int(input("Insira um número entre 0 e 5: "))
randomizado = random.randint(0, 5)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
if numero == randomizado:
    print("Parabéns, você acertou!")
else:
    print(f"Não foi desta vez, o número aleatório foi {randomizado}")
