contador_idade = 0
contador_men = 0
contador_woman = 0
print("="*25)
print("Cadastre pessoas!")
print("="*25)
while True: 
    while True:
        try:
            idade = int (input("Digite sua idade: ").strip())
            if idade <= 0 or idade > 120: 
                print("Idade invalida!")
            else: 
                if idade > 17:
                    contador_idade += 1 
                break
        except ValueError:
            print("Por favor, digite um número válido para a idade.")        
    while True:
        sexo = str(input("Digite seu sexo [M/F]: ").strip()).upper()
        if sexo != "M" and sexo != "F":
            print("sexo inválido!")  
        else:
            if sexo == "M":    
                contador_men += 1
            break 
    if sexo == "F" and idade < 20:
        contador_woman += 1
    
    while True:   
        print("="*25)
        continuar = str(input("Você quer cadastrar mais pessoas[S/N]: ")).upper()
        print("="*25)
        if continuar != "S" and continuar != "N":
            print("opção inválida! digite S/N!")
        else:
            break   
    if continuar == "N":
        break
print(f"foram {contador_idade} pessoa(s) maiores de 18! ")
print(f"foram {contador_men} homen(s) cadastrados:")
print(f"são {contador_woman} mulheres com menos de 20 anos")
       
            