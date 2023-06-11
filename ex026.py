"""Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra A, qual a primeira posição da letra e a ultima """
frase_user = input(str(("Digite uma frase: "))).lower().strip()
cont = frase_user.count('a')
print("A letra aparece A {} vezes na frase".format(cont))
position = frase_user.find('a')+1
print("A primeira letra apareceu na posição {} ".format(position))
print("A última posição da letra  é {} ".format(frase_user.rfind('a')+1))

