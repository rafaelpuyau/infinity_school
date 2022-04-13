'''
Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
'''

# Inicializo a variável em 0
somatorio = 0

# Laço for para ler 7 números inteiros
for num in range(1, 8):
    numero = int(input(f'{num}º número: '))
    somatorio += numero 

# Exibo na tela o somatório deles
print(f'Somatório: {somatorio}')
