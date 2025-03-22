valores = []
valor_procurado = 3
posicao = -1
vetor_par = []    
for i in range(4):
    while True:
        try:
            valor = int(input("Digite um valor inteiro: "))
            valores.append(valor)
            break
        except ValueError:
            print("Por favor, digite um valor inteiro válido.")
numero = valores.count(9)
if numero == 0:
    print(f"Não apareceu o número 9!")
elif numero == 1:
    print(f"Apareceu o número 9: {numero} vez!")
else:
    print(f"Apareceu o número 9: {numero} vezes") 




for i in range(len(valores)):   
    if valores[i] == valor_procurado:
        posicao = i
        print(f"A primeira ocorrência do número 3 está na posição {posicao + 1}!")
        break
if posicao == -1:
    print("Não tem ocorrência do número 3")
     
         




    
for i in valores: 
    if i % 2 == 0:
        vetor_par.append(i)
    else: 
        pass
print(f"Os valores pares são: {vetor_par}")


