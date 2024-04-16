contador = 0 
cont = int (0)
pr = int (1)
n = int( (input("Digite o numero do termo para ver a sequência: ")))
while contador < n:
    print (cont)
    proximo = cont + pr
    cont = pr
    pr = proximo
    contador += 1