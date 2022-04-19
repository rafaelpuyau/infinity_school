'''
Elaborar um algoritmo que captura 5 nomes na tela e adicione em uma lista. Exiba-os em seguida.
'''

nomes = []

for nome in range(5):
    nomes.append(input('Nome: ').title())

print(nomes)

for nome in nomes:
    print(nome)