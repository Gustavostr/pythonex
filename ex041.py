import datetime
ano_atual = datetime.datetime.now().year
nasc = int (input("Digite o ano de nascimento: "))
idade = ano_atual - nasc
if 1 < idade <= 9:
    print("Você está cadastrado(a) na categoria Mirim")
elif 9 < idade <= 14:
    print("Você está cadastrado(a) na categoria Infantil")
elif 14 < idade <= 19:
    print("Você está cadastrado(a) na categoria Junior")
elif 19 < idade <= 20:
    print ("Você está cadastrado(a) na categoria Sênior")
elif 20 < idade <= 120:
    print("Você está cadastrado(a) na categoria Master ")
elif idade > 120:
    print ("Idade invalida")
