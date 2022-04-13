'''
Faça um programa que leia um número inteiro e mostre o seu antecessor e o seu sucessor.
'''

# Leio o número e faço o casting para inteiro
numero = int(input('Digite um número: '))

# Imprimo na tela já fazendo a conta dentro do print
print(f'O antecessor de {numero} é {numero - 1}')
print(f'O sucessor de {numero} é {numero + 1}')

