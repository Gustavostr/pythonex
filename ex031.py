distancia_viagem = int(input("Qual a distancia da sua viagem em Km(apenas número): "))
if distancia_viagem <= 200:
    print("O preço dessa viagem é {} reais".format(0.50 * distancia_viagem))
else:
    print("O preço da sua viagem é {} reais".format(0.45 * distancia_viagem))

