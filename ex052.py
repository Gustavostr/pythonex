num = int (input("Digite um número inteiro positivo para verificar se é primo: "))
cont = 0
for c in range (1,num+1):
    divi = num/c
    if num%c == 0:
        cont += 1
    else: pass
if cont == 2: 
     print("É primo")
else: 
    print("Não é primo")
    