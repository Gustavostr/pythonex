nome = input("Digite seu nome completo: ")
print ("Seu nome em maisculas: {}".format(nome.upper()))
print("Seu nome em minúscula: {}".format(nome.lower()))
nm = ((nome.replace(" ", "")))
print ("O nome possui {} letras".format(len(nm)))
nome = nome.split()
print ("O primeiro nome é: {} e possui {} letras".format(nome[0],len (nome[0])))


