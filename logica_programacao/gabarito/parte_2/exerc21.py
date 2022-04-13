'''
Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens até 200km e R$0.45 para viagens mais longas.
'''

# Solicito a distância em km
distancia = int(input('Qual a distância que deseja percorrer [km]: '))

# Verifico se é maior que 200 km e aplico a taxa de R$0.45 por km.
# Senão, aplico a taxa de R$0.50 para viagens até 200 km.
if distancia > 200:
    preco_passagem = distancia * 0.45
else:
    preco_passagem = distancia * 0.50

# Imprimo na tela e formato o preço da passagem com 2 casas decimais
print(f'Preço da passagem de R${preco_passagem:.2f} para {distancia} km')
