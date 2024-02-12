vetor = []
for p in range(1,6,1):
    peso = float(input("Digite o peso de 5 pessoas: "))
    vetor.append(peso)
vetor.sort()

print ("O menor peso é {} e o maior peso é {}!".format(vetor[0],vetor[4]))
