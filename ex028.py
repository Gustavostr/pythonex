import random
dig = int(input("digite um número de 1 a 5 ") )
num = random.randint(1, 5)
if num == dig :
	print ("você ganhou na loteria")
else:
	print ( "\n você perdeu ")