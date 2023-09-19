salario = float(input("Digite o salário: "))
if salario > 1250.00:
	print ("Seu novo salário com aumento de 10% é {}!".format(salario*(10/100)+salario))
elif salario  < 1250.00:
	print ("Seu novo salário com 15% de aumento é {}!".format(salario*(15/100)+salario))
else: 
	print ("Erro digite novamente!")
