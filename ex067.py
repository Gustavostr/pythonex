tabuada = 0
while True: 
    tabuada = int(input("Digite qual tabuada quer consultar: "))
    if tabuada < 0:
        print("Tabuada encerreda!")
        break
    print ("="*25)
    for c in range (1, 11, 1):
        print(f"{c} X {tabuada} = {c*tabuada}")
    print ("="*25)