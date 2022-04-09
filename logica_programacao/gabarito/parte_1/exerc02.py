'''
Faça um programa que leia o nome do usuário, seu ano de nascimento, o ano atual e calcule a idade. Se a idade for maior ou igual a 18, imprima na tela o nome do usuário e a mensagem de entrada permitida (Ex. Fulano, sua entrada foi permitida). Se a idade for menor que 18 informar ao usuário que sua entrada não foi permitida (Ex. Fulano, sua entrada não foi permitida).
'''

# Solicito os dados ao usuário

# Não preciso de casting pois nome é uma string
nome_usuario = input('Nome: ')

# Casting para inteiro pois ano é um número inteiro
ano_nascimento = int(input('Ano de Nascimento: '))

# Casting para inteiro pois ano é um número inteiro
# No módulo de Python aprenderemos a usar a biblioteca 
# datetime para pegar automaticamento o ano atual
ano_atual = int(input('Ano Atual: '))

# Cálculo da idade
idade = ano_atual - ano_nascimento


# Bloco condicional

# Verifico se a idade é maior ou igual a 18
if idade >= 18:
    print(f'{nome_usuario}, sua entrada foi permitida')
else: # Entro no else quando a validação no if falhar
    print(f'{nome_usuario}, sua entrada NÃO foi permitida')
