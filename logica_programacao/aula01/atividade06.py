'''
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor
'''

# Defino 2 constantes
PERCENT_DIST = 0.28
IMPOSTOS = 0.45

# Leio o custo de fábrica de um carro
custo_fabrica = float(input('Custo de fábrica de um carro: '))

# Calculo o custo final do carro aplicando os percentuais
# Observe que custo_fabrica * PERCENT_DIST calcula os 28% sobre o custo de fábrica
# e também custo_fabrica * IMPOSTOS calcula os 45% sobre o custo de fábrica
custo_final = custo_fabrica + custo_fabrica * PERCENT_DIST + custo_fabrica * IMPOSTOS

# Imprimo na tela o custo final, formatando com 2 casas decimais

# f-string
print(f'Custo final do carro: R${custo_final:.2f}')

# format()
print('Custo final do carro: R${0:.2f}'.format(custo_final))
