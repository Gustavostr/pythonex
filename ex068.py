import random 
cont = 0
#Escolha do usuário
while True:
    while True:
        escolha_jd = str(input("Escolha PAR ou IMPAR: ").strip()).upper()
        if escolha_jd != "PAR" and escolha_jd != "IMPAR":
            print("Por favor, escolha PAR ou IMPAR.")
        else:
            break
    jogador = int (input ("Digite um número: "))


        
    # Escolha do compuador 
    computador = random.randint(1,10)
    if escolha_jd == "PAR":
        escolha_pc = "IMPAR"
    else:
        escolha_pc = "PAR"

    # Definição de par ou impar
    soma = jogador + computador
    resultado = soma % 2
    if resultado == 0:
        resultado_definitivo = "PAR"
    else: 
        resultado_definitivo = "IMPAR"

    #comparação dos jogadores
    if escolha_jd == resultado_definitivo:
        print(f"o jogador escolheu {escolha_jd}, e a maquina {escolha_pc} e o resultado foi {resultado_definitivo} ({soma}), portanto o Jogador venceu")
        cont += 1
    else:
        print(f"o jogador escolheu {escolha_jd}, e a maquina {escolha_pc} e o resultado foi {resultado_definitivo} ({soma}), portanto a Máquina venceu")
        
    if escolha_pc == resultado_definitivo:
        print(f"Jogo encerrado você teve {cont} vitórias consecutivas")
        break