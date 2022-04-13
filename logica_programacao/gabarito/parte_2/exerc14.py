'''
Faça um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro fumado. Calcule quantos dias de vida um fumante perderá e exiba o total de dias.
'''

qtde_cigarros = int(input('Quantos cigarros você fumava por dia? '))
qtde_anos = int(input('Quantos anos você já fumou? '))

# Regra de Negócio
# Fumante perde 10 min/cigarro fumado

# Multiplico a quantidade de cigarros fumados por dia pelo tempo de vida que perde (10 minutos)
# Assim sabemos o total de minutos a menos de vida por cigarro fumado
minutos_perdidos_dia = qtde_cigarros * 10 

# Cálculo de quantos dias pelos anos de fumo
dias_por_anos = qtde_anos * 365

# 1440 minutos = 1 dia, ou seja, 1h equivale a 60 min. Um dia tem 24h então 24 * 60 para saber os minutos de um dia
dias_perdidos = dias_por_anos * (minutos_perdidos_dia / 1440)

# Exibo a mensagem na tela fazendo o casting para inteiro de quantos dias o fumante já perdeu
print(f'Você já perdeu {int(dias_perdidos)} dias de vida por fumar {qtde_cigarros} cigarros por dia')