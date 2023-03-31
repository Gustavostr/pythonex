import math
num = float(input('Digite um numero qualquer para obter sua parte inteira: '))
print('A parte inteira de {} é {}'.format(num, math.trunc(num)))
#par = math.trunc(num)
#print('A parte inteira de {} é {}'.format(num, par))

# pode-se simplificar ainda mais colocando a função math.trunc no format do print assim:

# sendo assim não precisa-se alocar espaço na memória criando uma nova variável 


