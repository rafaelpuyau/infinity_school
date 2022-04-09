'''
Faça um programa que leia um número e retorne se ele é par, ímpar ou zero.
'''

# Leitura do número. Estou considerando apenas entradas inteiras
numero = int(input('Número: '))

# Bloco condicional
if numero == 0:
    print('ZERO')
# Verifico se o resto da divisão (%) é igual a zero. 
# Se for, o número é par
elif numero % 2 == 0:
    print('PAR')
else:
    print('ÍMPAR')
