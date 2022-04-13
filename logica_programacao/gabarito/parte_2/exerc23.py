'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo:

    O primeiro valor é o maior
    O segundo valor é o maior
    Não existe valor maior, os dois são iguais
'''

# Leio os números
num_1 = int(input('1º número: '))
num_2 = int(input('2º número: '))

# Teste qual número é maior.
# Se não houver um número maior que o outro, ele cai no else
if num_1 > num_2:
    print('O primeiro valor é maior')
elif num_2 > num_1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
