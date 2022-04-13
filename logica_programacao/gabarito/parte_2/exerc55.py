'''
Escreva um programa que leia um número qualquer e mostre a sua tabuada. Use a estrutura FOR.
'''

# Solicito um número ao usuário
numero = int(input('De qual número deseja ver sua tabuada? '))

for mult in range(1, 11):
    # Formatação da saída onde 2 representa o numero de casas ou espaços e o sinal >
    # informa o alinhamento do número. Substitua pelo sinal de < e veja como ficará a saída
    print(f'{numero} x {mult:>2} = {numero*mult:>2}')
    