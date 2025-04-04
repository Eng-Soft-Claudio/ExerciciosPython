print("=" * 40)
print(f'{"VALIDADOR DE EXPRESSÃO NUMÉRICA":^40}')
print("=" * 40)
lista = []
expressao = str(input("Digite uma expressão numérica: \n"))
for simbolo in expressao:
    if simbolo == "(":
        lista.append("(")
    elif simbolo == ")":
        lista.append(")")
parentese_aberto = lista.count("(")
parentese_fechado = lista.count(")")
if parentese_aberto == parentese_fechado:
    print("A expressão é válida.")
else:
    print("A expressão é inválida.")
print("=" * 40)