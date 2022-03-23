'''
Desenvolva um algoritmo que solicite o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato
'''

# Leio o preço de 3 produtos
produto1 = float(input('Preço do Produto 1 [R$]: '))
produto2 = float(input('Preço do Produto 2 [R$]: '))
produto3 = float(input('Preço do Produto 3 [R$]: '))

# Verifico qual produto é mais barato
if produto1 < produto2 and produto1 < produto3:
    print('Compre o Produto 1')
# Só preciso testar 1 sentença pois produto1 < produto2 falhou e produto 2 é menor que produto 1
elif produto2 < produto3:   
    print('Compre o Produto 2')
# Aqui o produto1 < produto3 falhou e produto2 < produto3 também falhou, logo produto3 é o mais barato
else:
    print('Compre o Produto 3')
