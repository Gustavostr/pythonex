i = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]
while i != "M" and i != "F":
    print("Digite uma letra válida!!")
    i = str(input("Digite seu sexo [M/F]: ")).upper().strip()[0]