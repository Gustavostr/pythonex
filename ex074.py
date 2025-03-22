import random
colection = []
for i in range (1,6):
    numeros = random.randint(0,1000)
    colection.append(numeros)
tupla = tuple(colection)
colection.sort()
print(tupla)
print(f"O menor número é: {colection[0]}")
print(f"O maior número é: {colection[4]}")
