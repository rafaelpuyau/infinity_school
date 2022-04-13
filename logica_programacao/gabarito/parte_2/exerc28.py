'''
Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:

    Carros populares (aluguel de R$90 por dia)
        Até 100km percorridos: R$0,20 por km
        Acima de 100km percorridos: R$0,10 por km
    Carros de luxo (aluguel de R$150 por dia)
        Até 200km percorridos: R$0,30 por km
        Acima de 200km percorridos: R$0,25 por km
'''

# Defino as constantes dos custos dos carros por dia
ALUGUEL_CARRO_POPULAR_DIA = 90
ALUGUEL_CARRO_LUXO_DIA = 150

# Inicializo a variável que receberá o cálculo do custo final
# Coloquei um valor de None mas poderia ter colocado 0
preco_cobrar = None

# Solicito as informações ao usuário
tipo_carro = input('Qual o tipo de carro [ Popular / Luxo ] ? ')
dias_aluguel = int(input('Quantos dias de aluguel? '))
km_percorridos = int(input('Quantos km percorridos? '))

# Verifico o tipo de carro e em seguida a km para realizar os cálculos
# Coloco o valor da variável tipo_carro como minúsculo
if tipo_carro.lower() == 'popular':
    if km_percorridos > 100:
        preco_cobrar = ALUGUEL_CARRO_POPULAR_DIA * dias_aluguel + km_percorridos * 0.10
    else:
        preco_cobrar = ALUGUEL_CARRO_POPULAR_DIA * dias_aluguel + km_percorridos * 0.20
elif tipo_carro.lower() == 'luxo':
    if km_percorridos > 200:
        preco_cobrar = ALUGUEL_CARRO_LUXO_DIA * dias_aluguel + km_percorridos * 0.25
    else:
        preco_cobrar = ALUGUEL_CARRO_LUXO_DIA * dias_aluguel + km_percorridos * 0.30

# Exibo na tela um resumo como fatura final para o cliente e coloco o valor da variável tipo_carro 
# com a 1ª letra em maiúscula
print('Fatura Final')
print(f'''
      Carro: {tipo_carro.capitalize()}
      Dias alugados: {dias_aluguel}
      Km percorridos: {km_percorridos}
      Valor a cobrar: R${preco_cobrar:.2f}
      ''')
