'''
Faça um programa que mostre na tela a seguinte contagem: 10 9 8 7 6 5 4 3 Acabou!
'''

# Laço for com a função range iniciando em 10, terminando em 2 (e não incluindo ele no iterável)
# e passo como -1 para que haja a contagem regressiva
for numero in range(10, 2, -1):
    print(numero, end=' ')

print('Acabou!')
