'''
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela. (Ex. Olá Rafael, seja muito bem-vindo!)
'''

# A função input retorna uma string
nome = input('Digite seu nome: ')

# Utilizamos o método title() para colocar as palvras com
# a primeira letra em maiúscula.
# Podiamos usar, também, o método capitalize() mas este 
# coloca apenas a primeira letra da primeira palavra em
# maiúscula.
# Teste com os 2 métodos com nomes compostos e veja a diferença
print(f'Olá {nome.title()}, seja muito bem-vindo!')
