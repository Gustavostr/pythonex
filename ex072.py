print(45 * "=")
print("Bem vindo \nCaixa 24H")
print("OBS: NOTAS DISPONÍVEIS 10,20,50 e 1")
print(45 * "=")
saque = int(input("Digite o valor que deseja sacar: "))
notas = [50, 20, 10, 1]

while saque > 0:
    for nota in notas:
        quantidade = saque // nota
        if quantidade > 0:
            print(f"{quantidade} notas de {nota}")
        saque = saque % nota
    if saque == 0:
        break
