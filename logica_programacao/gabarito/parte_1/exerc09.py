'''
Faça um programa que leia dois números e indique se são iguais ou se são diferentes. Mostre na tela o maior e o menor (nesta sequência).
'''

# Leitura dos números inteiros
# Estou considerando apenas números inteiros

# Casting para inteiro pois o retorno do input é string
num_1 = int(input('Número 1: '))
num_2 = int(input('Número 2: '))

# Bloco condicional
if num_1 == num_2:
    print('Os números são iguais')
else:
    print('Os números são diferentes')
    if num_1 > num_2:
        print(f'Maior: {num_1}, Menor: {num_2}')
    else:
        print(f'Maior: {num_2}, Menor: {num_1}')
