'''
Faça um programa que calcule e mostre na tela o somatório de 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
'''

# Inicializo a variável com 0
somatorio = 0

# A função range gera um iterável de 6 à 100 com saldo de 2
for numero in range(6, 101, 2):
    somatorio += numero

# Exibo na tela o somatório
print(f'O somatório é de {somatorio}')
