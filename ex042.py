medida1 = float(input("Digite uma medida: "))
medida2 = float(input("Digite mais uma medida: "))
medida3 = float(input("Digite a última medida: "))
if medida1 + medida2 > medida3 and medida1 + medida3 > medida2 and medida2 + medida3 > medida1:
    print("Temos um triângulo!!")
    if medida1 == medida2 == medida3:
        print("Temos um triangulo Equilatero!")
    elif medida1 == medida2 or medida2 == medida3 or medida1 == medida3:
     print("Temos um triangulo isósceles!")
    elif (medida1 != medida2 != medida3):
     print("temos um triangulo escaleno!")
else:
    print ("Não temos um triângulo!")