'''
Faça um programa que leia 6 números inteiros e no final mostre quantos são pares e quantos são ímpares.
'''

# Inicializo as variáveis que farão a contagem de pares e ímpares
pares = 0
impares = 0

breakpoint()

# Laço for para ler 6 números inteiros
for num in range(1, 7):
    numero = int(input(f'{num}º número: '))
    # Verifico se número é par. Se for verdadeiro, adiciono 1 à variável pares
    if numero % 2 == 0:
        pares += 1
    # Se falso, adiciono 1 à variável ímpares
    else:
        impares += 1

# Exibo na tela o resultado 
print(f'Foram digitados {pares} pares e {impares} ímpares')
