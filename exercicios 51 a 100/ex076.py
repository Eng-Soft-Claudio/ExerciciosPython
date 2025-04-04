tupla = (
    "Arroz (5kg)", 20.00,
    "Feijão (1kg)", 8.00,
    "Macarrão (500g)", 4.50,
    "Óleo de Soja (900ml)", 7.00,
    "Açúcar (1kg)", 4.00,
    "Sal (1kg)", 2.50,
    "Café (500g)", 12.00,
    "Leite (1L)", 5.50,
    "Margarina (500g)", 6.00,
    "Pão de Forma", 7.00,
    "Queijo Mussarela (kg)", 35.00,
    "Presunto (kg)", 30.00,
    "Manteiga (200g)", 8.50,
    "Iogurte (unidade)", 2.00,
    "Frango Inteiro (kg)", 12.00,
    "Carne Bovina (kg)", 35.00,
    "Linguiça (kg)", 18.00,
    "Ovos (dúzia)", 10.00,
    "Tomate (kg)", 6.00,
    "Cebola (kg)", 5.00,
    "Batata (kg)", 4.50,
    "Alface (unidade)", 2.50,
    "Banana (kg)", 4.00,
    "Maçã (kg)", 7.00,
    "Laranja (kg)", 3.50,
    "Detergente (500ml)", 2.00,
    "Sabão em Pó (1kg)", 8.00,
    "Amaciante (2L)", 10.00,
    "Desinfetante (500ml)", 3.00,
    "Papel Higiênico (4 rolos)", 5.50,
    "Creme Dental (90g)", 3.50,
    "Shampoo (350ml)", 12.00,
    "Sabonete (unidade)", 1.50,
    "Desodorante (150ml)", 10.00,
    "Absorvente (pacote)", 6.00,
    "Fralda Descartável (pacote)", 30.00,
    "Água Sanitária (1L)", 3.00,
    "Esponja de Aço (unidade)", 1.00,
    "Papel Alumínio (15m)", 8.00,
    "Filme Plástico (15m)", 6.50,
    "Guardanapo de Papel (pacote)", 3.00,
    "Farinha de Trigo (1kg)", 5.00,
    "Fermento em Pó (100g)", 2.50,
    "Biscoito Recheado (pacote)", 3.50,
    "Chocolate em Barra (90g)", 5.00,
    "Refrigerante (2L)", 8.00,
    "Suco de Fruta (1L)", 6.00,
    "Cerveja (350ml)", 3.00,
    "Água Mineral (1.5L)", 2.00
)


print("=" * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print("=" * 40)
for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f"{tupla[i]:.<31}", end="")
    else:
        print(f"R${tupla[i]:>7.2f}")
print("=" * 40)
