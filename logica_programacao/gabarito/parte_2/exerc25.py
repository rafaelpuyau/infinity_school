'''
Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:

    Até 3 anos de empresa: aumento de 3%
    Entre 3 e 10 anos: aumento de 12.5%
    10 anos ou mais: aumento de 20%
'''

# Leio os dados solicitados
nome_funcionario = input('Nome do funcionário: ')
salario = float(input('Salário [R$]: '))
anos_trabalhados = int(input('Anos que traballha na empresa: '))

# Verifico o tempo que o funcionário trabalha na empresa e aplico os percentuais de acordo com o enunciado
if anos_trabalhados >= 10:
    novo_salario = salario * 1.20
elif anos_trabalhados > 3:
    novo_salario = salario * 1.125
else:
    novo_salario = salario * 1.03

# Exibo na tela o salário reajustado formatado com 2 casas decimais
print(f'{nome_funcionario} com salário reajustado de R${novo_salario:.2f}')
