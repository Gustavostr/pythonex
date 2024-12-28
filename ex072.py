extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = 80

while numero < 0 or numero > 20:
    try:
        numero = int(input("Digite um número inteiro de 0 a 20! "))
        print(f"você digitou o número {extenso[numero]}!")
    except ValueError:
        print(" Erro! Digite um numero inteiro ")
    except IndexError:
        print("Digite um numero entre 0 e 20! ")


