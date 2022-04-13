'''
Faça um programa usando a estrutura FOR que leia um número inteiro positivo e mostre na tela uma contagem de 0 até o valor digitado, inclusive.
'''

# Solicito um número
numero = int(input('Deseja contar até quanto? '))

# Para que esse número seja incluído no iterável gerado pela função range, basta somar 1 a ele
for num in range(0, numero + 1):
    print(num, end=' ')
