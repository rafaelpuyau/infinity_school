'''
Ler o nome de 2 times e o número de gols marcados na partida (para cada time).
Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE
'''

# Leio os times e os gols marcados por cada um
time1 = input('1º time: ')
gols_time1 = int(input('Quantos gols marcou? '))

time2 = input('2º time: ')
gols_time2 = int(input('Quantos gols marcou? '))

# Verifico qual time fez mais gols
if gols_time1 > gols_time2:
    print(f'{time1} VENCEU a partida!')
elif gols_time2 > gols_time1:
    print(f'{time2} VENCEU a partida!')
else:
    print('EMPATE')
    