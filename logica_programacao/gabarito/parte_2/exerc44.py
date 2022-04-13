'''
Faça um programa que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
'''

# Inicializo as variáveis com valor 0
maior = 0
menor = 0 

# Laço for para ler os 8 preços dos produtos.
for preco in range(1, 9):
    preco_lido = float(input(f'Preço do produto ({preco}) [R$]: '))
    # Coloco o primeiro preço lido nas duas variáveis
    if preco == 1:
        maior = preco_lido
        menor = preco_lido
    # A partir do segundo preço lido eu já posso fazer as comparações
    else:
        if preco_lido > maior:
            maior = preco_lido
        elif preco_lido < menor:
            menor = preco_lido

# Exibo na tela os valores do maior e menor preço
print(f'Maior preço: R${maior:.2f}')
print(f'Menor preço: R${menor:.2f}')
