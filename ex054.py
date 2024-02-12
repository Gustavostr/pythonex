import datetime
cont = 0
cost = 0
ano_atual = datetime.datetime.now().year
for i in range(1,8,1):
    ano = int(input("Digite o ano de nascimento da {}ª pessoas:  ".format(i)))
    
    if ano_atual - ano > 18:
        cont += 1    
    else: 
        cost += 1
print("Temos {} pessaos maior de 18! ".format(cont))
print("Temos {} pessaos menores de 18!".format(cost))