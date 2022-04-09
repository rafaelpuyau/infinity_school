'''
Faça um programa que imprima 20 números (de 1 à 20) em ordem crescente e um do lado do outro.
'''

# Uso a estrutura for pois eu sei quantas vezes preciso 
# repetir essa impressão na tela.

# Range com start em 1 (inclusive) e end em 21 (não incluído) na formação do iterável
for numero in range(1, 21):
    print(numero, end=' ')
