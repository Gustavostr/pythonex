frase = str(input("Digite a frase para verificar palíndromo: "))
s_aglutinada = frase.replace(" ", "")
s_invertida = "".join(reversed(s_aglutinada))
if s_invertida == s_aglutinada:
    print("temos um palíndromo!")
else :
    print("não temos um palíndromo!")
