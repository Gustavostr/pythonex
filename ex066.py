cont = 0
soma = 0
print ("Digite um número inteiro entre 1 e 998")
while True:
    numero = int(input("Digite um número inteiro [999 para sair]: "))
    if numero == 999:
        break 
    cont +=1
    soma += numero
print(f"Foram digitado(s) {cont} e a somma deu {soma}!")