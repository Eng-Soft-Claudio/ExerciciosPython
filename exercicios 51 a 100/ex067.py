print("=" * 30)
print("   TABUADA DE MULTIPLICAÇÂO")
while True:
    print("=" * 30)
    termo = int(input("Informe um número: "))
    if termo < 0:
        print("=" * 30)
        print("   PROGRAMA ENCERRADO")
        break
    for n in range(1, 11):
        print(f"{termo:2} X {n:2} = {(termo * n):3}")