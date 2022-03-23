'''
Solicite um número ao usuário e mostre se o número é positivo ou negativo.

ATENÇÃO : o zero é considerado um número neutro e o nosso usuário não irá digitá-lo quando 
solicitado
'''

# Solicito ao usuário um número
numero = int(input('Digite um número: '))

# Verifico se este número é positivo ou negativo
if numero > 0:
    print('Número positivo')
else:
    print('Número negativo')
