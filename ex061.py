termo = int(input("Digite o primeiro termo da P.A: "))
razao = int (input("digite a razão da P.A: "))
cont = int(0)
while cont < 11:
    cont += 1
    cont = termo + (10-1) * razao
    print("O décimo termo da P.A é {}".format(cont))
    