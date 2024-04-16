num = 0
lista = []
contador = int(0)
while num != 999:
    num = int(input("Digite os números de 0 a 999: "))
    if num < 0 or num >= 1000:
        print("Valor inválido!")
    elif num != 999: 
        lista.append(num)
        soma = sum(lista)
        contador += 1
print("A soma dos numeros é {} e foram digitador {} números".format(soma,contador))
    
