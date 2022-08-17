'''
Crie uma função que dado uma data digitada pelo usuário, informe há quantos dias atrás aconteceu aquela data.
'''

from datetime import datetime

data = input('Informe uma data: ')

conv_data = datetime.strptime(data, '%d/%m/%Y')
data_atual = datetime.today().now()

dias = data_atual - conv_data

print(f'{datetime.strftime(conv_data, "%d/%m/%Y")} ocorreu há {dias.days} dias atrás')
3