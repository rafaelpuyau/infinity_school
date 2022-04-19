'''
Elaborar um algoritmo que captura 10 valores inteiros na tela e adicione-os em uma lista. Exiba apenas os ímpares.
'''

numeros = list()

for num in range(10):
    numeros.append(int(input('Número: ')))


for num in numeros:
    if num % 2 != 0:
        print(num)

