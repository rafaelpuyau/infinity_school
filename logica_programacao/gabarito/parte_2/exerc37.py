'''
Faça um programa que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores deste intervalo. Ex. valor inicial de 3, valor final de 10 e incremento de 2. A saída será: 3 5 7 9 Fim da contagem!
'''

inicio = int(input('Início da contagem: '))
fim = int(input('Fim da contagem: '))
passo = int(input('Passo da contagem: '))

for numero in range(inicio, fim, passo):
    print(numero, end=' ')

print('Fim da contagem!')