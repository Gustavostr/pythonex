import random, time
print("=============Jokenpô=============")
print ("Escola sua opção: \n 1 - Pedra \n 2 - papel \n 3 - Tesoura")
pc = ['Pedra', 'Papel', 'Tesoura']
pces = random.choice(pc)
user = int (input())

if user == 1:
    time.sleep(0.7)
    print ("jo")
    time.sleep(0.7)
    print ("ken")
    time.sleep(0.9)
    print("pô!!")
    escolha = 'Pedra'
    print('-='*20)
    print("você escolheu {}".format(escolha))
    print("O  computador escolheu {}".format(pces))
    print('-='*20)
    if pces == 'Papel':
        print("A maquina ganhou")
    elif pces == 'Pedra':
        print ("Deu empate")
    elif pces =='Tesoura' :
        print("Voce ganhou")
        
elif user == 2:
    time.sleep(0.7)
    print ("jo")
    time.sleep(0.7)
    print ("ken")
    time.sleep(0.9)
    print("pô!!")
    escolha = 'Papel'
    print('-='*20)
    print("você escolheu {}".format(escolha))
    print("O  computador escolheu {}".format(pces))
    print('-='*20)
    if pces == 'Tesoura':
        print ("A maquina ganhou")
    elif pces == 'Papel':
        print("Deu empate")
    elif pces == 'Pedra':
        print("Você ganhou:")
        
    
elif user == 3:
    time.sleep(0.7)
    print ("jo")
    time.sleep(0.7)
    print ("ken")
    time.sleep(0.9)
    print("pô!!")
    escolha = 'Tesoura'
    print('-='*20)
    print("você escolheu {}".format(escolha))
    print("O  computador escolheu {}".format(pces))
    print('-='*20)
    if pces == 'Pedra':
        print("A maquina ganhou")
    elif pces == 'Tesoura':
        print ("Deu empate")
    elif pces == 'Papel':
        print("Você ganhou!!!")
    
else:
    print ("opção invalida")




