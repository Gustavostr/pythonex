peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em M: "))
imc = peso/altura**2
if imc < 18.5:
    print("Seu IMC É {:.1f} portanto, Você está abaixo do peso".format(imc))
elif 18.5 < imc < 25:
    print("Seu IMC É {:.1f} portanto, Seu peso está normal!!".format(imc))
elif 25 < imc < 30:
    print("Seu IMC É {:.1f} portanto, Você está com sobrepeso!".format(imc))
elif 30 < imc < 40:
    print(" Seu IMC É {:.1f} portanto, Você está com obesidade!".format(imc))
elif imc > 40:
    print("ATENÇÃo! Seu IMC É {:.f} portanto, Você está com obesidade mórbida".format(imc))

