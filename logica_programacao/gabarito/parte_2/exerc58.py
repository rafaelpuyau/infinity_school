'''
[ DESAFIO ] Faça um programa que mostre os 10 primeiros elementos da Sequência de Fibonacci: 0 1 1 2 3 5 8 13 21 34
'''

# Inicializo as variáveis
a = 0 
b = 1

# Exibo na tela as 2 primeiras
print(a, b, end=' ')

# Range vai até 8 pq já imprimi as 2 primeiras
for el in range(8):
    c = a + b
    # Faço o desempacotamento, onde a recebe o valor de b e b recebe o valor de c
    a, b = b, c
    print(c, end=' ')
