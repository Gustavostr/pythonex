cidade = str(input("Digite o nome de uma cidade: "))
cidade = cidade.title()
cidade = cidade.split()
if cidade[0] == str("Santo"):
	print("\n Essa cidade é santa")
else:  
	print("\n essa cidade, infelizmente, não é santa")