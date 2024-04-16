lista = []
quest = str("S")
contador = int(0)
while quest == "S": 
    num = int (input("Digite números inteiros: "))
    quest = str (input("Deseja continuar S/N? ")).upper().strip()[0]
    lista.append(num)
    lista.sort()
    contador += 1
    media = (sum(lista))/ contador
print("A média da lista é {:.2f}, o primeiro termo é {} e o último termo é {}".format(media,lista[0],lista[-1]))
