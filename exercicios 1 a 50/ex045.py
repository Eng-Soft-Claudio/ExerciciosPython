
import random
print("=-=-= JOKENPÔ =-=-=")
print("Escolha:\n1 -- PAPEL\n2 -- PEDRA\n3 -- TESOURA")
print("=-=-= JOKENPÔ =-=-=")
escolha = int(input("Informe sua escolha: "))
computador = random.randint(1,3)
while escolha < 1 or escolha > 3:
    print("Opção inválida...")
    escolha = int(input("Informe sua escolha: "))
if escolha == 1:
    print("Você escolheu PAPEL...")
elif escolha == 2:
    print("Você escolheu PEDRA...")
elif escolha == 3:
    print("Você escolheu TESOURA...")
if computador == 1:
    print("O computador escolheu PAPEL...")
elif computador == 2:
    print("O computador escolheu PEDRA...")
elif computador == 3:
    print("O computador escolheu TESOURA...")
if escolha == 1 and computador == 1:
    print("Empate...")
elif escolha == 1 and computador == 2:
    print("Ganhou...")
elif escolha == 1 and computador == 3:
    print("Perdeu...")
elif escolha == 2 and computador == 1:
    print("Perdeu...")
elif escolha == 2 and computador == 2:
    print("Empate...")
elif escolha == 2 and computador == 3:
    print("Ganhou...")
elif escolha == 3 and computador == 1:
    print("Ganhou...")
elif escolha == 3 and computador == 2:
    print("Perdeu...")
elif escolha == 3 and computador == 3:
    print("Empate...")
    
    