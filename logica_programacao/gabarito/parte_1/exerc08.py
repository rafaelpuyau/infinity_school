'''
Faça um programa que leia o dia, o mês e o ano (todos sendo valores núméricos e inteiros) e imprima a data nos seguintes formatos: 31/3/2022 e 31.3.2022.
'''

# Leitura dos dados solicitados
dia = int(input('Dia: '))
mes = int(input('Mẽs: '))
ano = int(input('Ano: '))

# Usar o parâmetro sep com os valores / e .
print(dia, mes, ano, sep='/')
print(dia, mes, ano, sep='.')
