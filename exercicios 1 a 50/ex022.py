nome_completo = str(input("Digite seu nome completo: ")).strip()
print(f"Seu nome em letras maiúsculas é {nome_completo.upper()}")
print(f"Seu nome em letras minúsculas é {nome_completo.lower()}")
nome_formatado = nome_completo.split()
print(f"Seu nome possui ao todo {len(nome_completo) - nome_completo.count(" ")} letras.")
print(f"Seu primeiro nome é {nome_formatado[0]} e possui {nome_completo.find(" ")} letras.")

