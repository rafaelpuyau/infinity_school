'''
Faça um programa que leia a largura e altura de uma parede, calcule mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

# Leitura dos dados e casting para o tipo de dado correto
largura = float(input('Largura: '))
altura = float(input('Altura: '))

# Cálculo da área da parede e da quantidade de tinta
area = largura * altura
qtde_tinta = area / 2

print(f'Área a ser pintada: {area:.2f}m²')
print(f'Quantidade de tinta para o serviço: {qtde_tinta:.2f} litro(s)')
