import math
import random
aluno = input("Digite o nome do primeiro aluno: ")
aluno1 = input("Digite o nome do segundo aluno: ")
aluno2 = input("Digite o nome do terceiro aluno: ")
aluno3 = input("Digite o nome do quarto aluno: ")
lista = [aluno, aluno1, aluno2, aluno3]

random.shuffle(lista)

print('O escolhido é {}'.format(lista))
