import datetime
ano_nascimento = int(input("Informe seu ano de nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    print(f"Você tem apenas {idade} anos de idade. Ainda falta {18 - idade} anos para se alistar no serviço militar.")
elif idade == 18:
    print(f"Você já possui {idade} anos de idade. Chegou a hora de se alistar no serviço militar.")
else:
    print(f"Você possui {idade} anos de idade. Passou {idade - 18} anos da idade de alistamento. Procure a junta militar mais próxima.")