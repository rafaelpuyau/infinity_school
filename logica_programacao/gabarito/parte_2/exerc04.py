'''
Faça um programa que leia dois números inteiros e faça as 4 operações básicas (adição, subtração, multiplicação e divisão) entre esses 2 números mostrando na tela como o exemplo à seguir: A soma entre 3 e 4 é igual a 7.
'''

# ATENÇÃO : Não estamos considerando o número zero como
# valor de entrada do usuário

# Casting para inteiro pois o input retorna string
num_1 = int(input('Digite um número: '))
num_2 = int(input('Agora digite outro número: '))

# Atribuição do resultado das operações nas variáveis correspondentes
soma = num_1 + num_2
subtracao = num_1 - num_2
multiplicacao = num_1 * num_2
divisao = num_1 / num_2

print(f'A soma entre {num_1} e {num_2} é igual a {soma}')
print(f'A subtração entre {num_1} e {num_2} é igual a {subtracao}')
print(f'A multiplicação entre {num_1} e {num_2} é igual a {multiplicacao}')
print(f'A divisão entre {num_1} e {num_2} é igual a {divisao}')

# Outra forma de exibir o resultado e fazendo a operação diretamente no print
print(f'A soma entre {num_1} e {num_2} é igual a {num_1 + num_2}')
print(f'A subtração entre {num_1} e {num_2} é igual a {num_1 - num_2}')
print(f'A multiplicação entre {num_1} e {num_2} é igual a {num_1 * num_2}')
print(f'A divisão entre {num_1} e {num_2} é igual a {num_1 / num_2}')