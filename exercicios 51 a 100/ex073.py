clubes_brasileirao_2024 = (
    "Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional",
    "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama",
    "Vitória", "Atlético Mineiro", "Fluminense", "Grêmio", "Goiás",
    "Santos", "Athletico Paranaense", "Criciúma", "Atlético Goianiense", "Cuiabá"
)
print(f"\nOs 5 primeiros colocados do Campeonato 2024 {clubes_brasileirao_2024[0:5:]}\n")
print(f"Os 4 clubes rebaixados: {clubes_brasileirao_2024[-4::]}\n")
print(f"O Palmeiras terminou em {clubes_brasileirao_2024.index("Palmeiras") + 1}º colocado.\n")
print(f"A lista de times que participaram do campeonato em ordem alfabética: {sorted(clubes_brasileirao_2024)}")