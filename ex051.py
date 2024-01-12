termo = int (input("Digite o primeiro termo da P.A: "))
razao = int (input("digite a razão da P.A: "))
dec = termo + (11-1) * razao
for c in range (termo,dec,razao):
    print(c)