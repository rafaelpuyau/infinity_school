'''
Faça um programa que leia o preço de um produto, calcule e mostre o seu preço promocional, com desconto de 5%.
'''

# Constante
# 5% = 0.05
PERCENTUAL = 0.05

# Leio o preço do produto e faço o casting para float
preco_produto = float(input('Preço do produto: R$'))

# Cálculo do desconto e do preço promocional
desconto = preco_produto * PERCENTUAL
preco_promocional = preco_produto - desconto

# Formato a saída do preço promocional com 2 casas decimais 
# Casting do percentual para float e formato com 1 casa decimal para mostrar na tela
print(f'Preço promocional de R${preco_promocional:.2f} com desconto de {float(PERCENTUAL*100):.1f}%')
