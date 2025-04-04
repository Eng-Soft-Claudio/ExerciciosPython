lista = []
for n in range (4):
    lista.append(int(input(f"Informe o {n + 1}º valor: ")))
tupla = tuple(lista)
if 9 not in tupla:
    print("Não foi digitado nenhum número 9")
else:
    print(f"Quantas vezes apareceu o número 9?\n Apareceu {tupla.count(9)} vezes")
if 3 not in tupla:
    print("Não foi digitado nenhum número 3")
else:    
    print(f"Em que posição foi digitado o primeiro número 3?\n Foi digitado na posição {tupla.index(3) + 1}")
print("Números pares digitados: ")
for n in range (len(tupla)):
    if tupla[n] % 2 == 0:
        print(" ", tupla[n])
    

