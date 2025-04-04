import random
import time

numero = random.randint(1, 9999)
print("~" * 39)
print("| Gerando um número aleatório...      |")
time.sleep(1)
print("| ...                                 |")
time.sleep(1)
print("| ...                                 |")
time.sleep(1)
print("| ...                                 |")
time.sleep(1)
print(f"| O número gerado foi:     {numero}       |")
print("~" * 39)
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print("| MILHAR | CENTENA | DEZENA | UNIDADE |")
print(f"|{milhar:7} | {centena:^7} | {dezena:^6} | {unidade:^7} |")

print("~" * 39)
