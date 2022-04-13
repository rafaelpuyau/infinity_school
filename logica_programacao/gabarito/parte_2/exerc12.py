'''
A locadora de carros - Infinity Car - precisa da sua ajuda para cobrar por seus serviços. Faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$95 por dia e R$0,35 por km rodado.
'''

# Constantes
CUSTO_CARRO = 95
KM_RODADO = 0.35

# Leio as variáveis solicitadas
km_percorridos = int(input('Km Percorridos: '))
aluguel = int(input('Quantos dias de aluguel? '))

# Cálculos por Km e por dia de aluguel
custo_por_km = km_percorridos * KM_RODADO
custo_carro_por_dia = aluguel * CUSTO_CARRO

# Cálculo do total a pagar
total_a_pagar = custo_carro_por_dia + custo_por_km

print(f'Preço total a pagar R${total_a_pagar:.2f}')
