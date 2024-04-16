import random
num = random.randint(1, 5)
dig = int(input("digite um número de 1 a 5 ") )
while num != dig:
    dig = int(input("Errou!! digite um número de 1 a 5 ") )
    if num == dig: 
        print("Você ganhou!!")

