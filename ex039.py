import datetime
ano_atual = datetime.datetime.now().year
ano_nasc = int(input("Digite o ano que você nasceu: "))
idade = ano_atual - ano_nasc
if idade > 18:
    print("Já passou o tempo de alistamento! \nprocure a junta mais próxima para regularizar a situação!")
    print("passou {} anos!!".format(idade - 18))
elif idade < 18:
    print("Não chegou a hora de se alistar ainda!!")
    print ("Falta {} ano(os) para se alistar".format(18 - idade))
elif idade == 18:
    print ("Está na hora de se alistar!! \n vá até a junta mais proxima")


