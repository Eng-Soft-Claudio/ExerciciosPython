from time import sleep
print("-=" * 15)
print("         BANCO DO POVO")
print("-=" * 15)
print("Informe o valor do saque:")
saque = int(input(" R$"))
total_saque = saque
print("~~" * 15)
sleep(1)
print(" Processando...")
sleep(1)
print("...")
sleep(1)
print("...")
sleep(1)
cedulas = 50
total_cedulas = 0
while True:
    if total_saque >= cedulas:
        total_saque -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} de R${cedulas:.2f}")
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total_saque == 0:
            break
print("~~" * 15)
