'''
Faça um programa que leia quanto de dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares e euros ela pode comprar. Considere as cotações de US$1 = R$4.79 e €1 = R$5.33.
'''

# Constantes
DOLAR = 4.79
EURO = 5.33

# Solicito quanto em dinheiro o usuário tem na carteira
carteira = float(input('Quanto você tem na carteira [R$]? '))

# Faço as conversões
conv_em_dolar = carteira / DOLAR
conv_em_euro = carteira / EURO 

# Imprimo na tela quanto o usuário pode comprar de cada moeda
print(f'Com R${carteira:.2f} você pode comprar US${conv_em_dolar:.2f} e €{conv_em_euro:.2f}')
