termo = int(input("Digite o primeiro termo da P.A: "))
razao = int (input("digite a razão da P.A: "))
cont = int(0)
ultimo_termo = int (input ("Digite o termo que você quer achar: "))
while ultimo_termo != 0:
    cont = termo + (ultimo_termo-1) * razao
    print("O termo da P.A é {}".format(cont))
    ultimo_termo = int (input ("Digite o termo que você quer achar: "))
print("Fim")