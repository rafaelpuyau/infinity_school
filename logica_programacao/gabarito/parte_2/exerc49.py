'''
Faça um programa que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa deve perguntar ao usuário se ele quer continuar ou não a ler os dados dos funcionários.
'''

# Inicialização das variáveis que receberão as somas dos salários
salarios_pagos_homens = 0
salarios_pagos_mulheres = 0

# Laço while com a condição True
while True:
    salario = float(input('Salário do funcionário [R$]: '))
    # Solicito o dados do usuário. A função input retorna uma string (que é um iterável)
    # Uso a função lower() para colocar tudo em minúsculas e pego o primeiro elemento desse iterável com o índice 0
    sexo = input('Qual o sexo? ').lower()[0]
    
    # Comparo se o dado lido é de um homen ou de uma mulher e realizo a soma
    if sexo == 'm':
        salarios_pagos_homens += salario
    elif sexo == 'f':
        salarios_pagos_mulheres += salario
    
    # Pegunto ao usuário se deseja continuar lendo
    # Uso a função lower() para colocar em minúsculas e pego a primeira letra através do índice 0
    escolha = input('Deseja continuar lendo os dados dos funcionários? [S/N] ').lower()[0]
    
    # Se o retorno for n, saio do laço com break
    if escolha == 'n':
        break

# Exibição dos salários pagos aos homens e mulheres
print(f'Total de salários pagos às mulheres: R${salarios_pagos_mulheres:.2f}')
print(f'Total de salários pagos aos homens: R${salarios_pagos_homens:.2f}')
