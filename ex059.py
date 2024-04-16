escolha_usuario = 0
num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro valor: "))
while escolha_usuario == 0:
	opcao = int(input("Escolha a operação abaixo: \n [1] Somar \n [2] Multiplicar \n [3] Maior \n [4] Outros números \n [5] Sair do progama \n"))

	if opcao == int(1): 
		escolha_usuario = int(1) 
		print("A soma é {}!".format(num1 + num2))
	elif opcao == int (2):
		escolha_usuario = int(2)
		print("A multiplicação é {}!".format(num1 * num2))
	elif opcao == 3:
		escolha_usuario = 3
		if num1 > num2: 
			print("O número {} é maior".format(num1))
		else: 
			print("O número {} é maior!".format(num2))
	elif opcao == 4:
		escolha_usuario = 0
		num1 = float(input("Digite um numero: "))
		num2 = float(input("Digite outro valor: "))
	elif opcao == int(5):
		escolha_usuario = 5
		print("Aplicação encerrada!!")
	else:
		print("valor inválido!!")

		 
	