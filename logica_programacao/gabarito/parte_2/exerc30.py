'''
Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:

    Mulheres:
        menos de 15 anos de empresa: +5%
        de 15 até 20 anos de empresa: +12%
        mais de 20 anos de empresa: +23%
    Homens:
        menos de 20 anos de empresa: +3%
        de 20 até 30 anos de empresa: +13%
        mais de 30 anos de empresa: +25%
'''

# Leio as informações solicitadas
salario_atual = float(input('Salário atual [R$]: '))
genero = input('Gênero [ masculino / feminino ]: ')
tempo_empresa = int(input('Tempo de empresa [em anos]: '))

# Verifico os critérios da empresa para o cálculo do reajuste
if genero.lower() == 'mulheres':
    if tempo_empresa > 20:
        salario_reajustado = salario_atual * 1.23
    elif tempo_empresa < 15:
        salario_reajustado = salario_atual * 1.05
    else:
        salario_reajustado = salario_atual * 1.12
else:
    if tempo_empresa > 30:
        salario_reajustado = salario_atual * 1.25
    elif tempo_empresa < 20:
        salario_reajustado = salario_atual * 1.03
    else:
        salario_reajustado = salario_atual * 1.13

# Exibo na tela o salário reajustado de acordo com os critérios da empresa
# Formato o salário reajustado com 2 casas decimais 
print(f'Salário reajustado R${salario_reajustado:.2f}')
