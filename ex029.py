velocidade_carro = float (input("Digite a velociddade do carro: "))
if velocidade_carro > 80:
    print("Você foi multado!! \nVocê foi multado em {} reais!".format((velocidade_carro-80)*7))
else:
    print("Verde")
