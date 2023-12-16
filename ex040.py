nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))
media = float((nota_1 + nota_2)/2)
if media < 5:
    print("sua média foi {}, portanto está reprovado!".format(media))
elif 5 < media < 7:
    print ("sua nota foi {:.2f}, portanto você está em recuperação".format(media))
elif 7 < media < 10:
    print("Parabéns sua media foi {}, portanto você está aprovado".format(media))
elif media > 10:
    print("nota invalida! tente novamente")

    
