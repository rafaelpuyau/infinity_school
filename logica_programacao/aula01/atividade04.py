'''
Escreva um algoritmo para ler um número total de eleitores de um município, o número de 
votos em branco, nulos e válidos.

Calcular e escrever o percentual que cada um representa em relação ao total de eleitores
'''

# Solicito a entrada de dados
total_eleitores = int(input('Total de eleitores: '))
votos_brancos = int(input('Quantidade de votos em branco: '))
votos_nulos = int(input('Quantidade de votos nulos: '))
votos_validos = int(input('Quantidade de votos válidos: '))

# Calculo os percentuais
percent_brancos = votos_brancos / total_eleitores * 100
percent_nulos = votos_nulos / total_eleitores * 100
percent_validos = votos_validos / total_eleitores * 100

# Imprimo na tela os percentuais dos votos formatados com 2 casas decimais

# f-string
print(f'Votos em branco : {percent_brancos:.2f}% de {total_eleitores} eleitores')
print(f'Votos nulos : {percent_nulos:.2f}% de {total_eleitores} eleitores')
print(f'Votos válidos : {percent_validos:.2f}% de {total_eleitores} eleitores')

# Separador
print('-' * 50)

# format()
print('Votos em branco : {0:.2f}% de {1} eleitores'.format(percent_brancos, total_eleitores))
print('Votos nulos : {0:.2f}% de {1} eleitores'.format(percent_nulos, total_eleitores))
print('Votos válidos : {0:.2f}% de {1} eleitores'.format(percent_validos, total_eleitores))
