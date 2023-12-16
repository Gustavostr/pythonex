num = int(input("Digite um número inteiro para converter: "))
selecao_convert = int(input("Digite a opção que você quer converter: \n 1 - Binário\n 2 - Octal\n 3- Hexadecimal\n"))
if selecao_convert == 1:
  print ("Você escolheu a base Binária!")
  print (format(num, 'b'))
  
  
elif selecao_convert == 2:
	print("Você escolheu a base Octal")
	print (format(num, 'o'))
	
elif selecao_convert == 3:
	print("Você escolheu a base Hexadecimal")
	print(format(num, 'x'))
	
else: print ("opção inválida")


