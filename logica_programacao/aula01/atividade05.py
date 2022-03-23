'''
Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis
'''

# Inicializo as variáveis com os valores solicitados no enumciado
a = 10
b = 20

# Crio uma variável auxilar para realizar a troca
aux = a 
a = b 
b = aux 

# Imprimo na tela os valores novos

# f-string
print(f'A tinha 10 e agora tem {a}')
print(f'B tinha 20 e agora tem {b}')

# Separador
print('-' * 30)

# format()
print('A tinha 10 e agora tem {}'.format(a))
print('B tinha 20 e agora tem {}'.format(b))
