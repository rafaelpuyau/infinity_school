'''
Faça um programa que leia o salário de um funcionário, calcule e mostre na tela seu novo salário com 15% de aumento.
'''

# Constante
PERCENTUAL_AUMENTO = 0.15

# Leitura e casting do salário para float
salario = float(input('Salário: '))

# Calculo o novo salário
novo_salario = salario + (salario * PERCENTUAL_AUMENTO)

# Imprimo na tela e formato o salário com 2 casas decimais
print(f'Salário com 15% de aumento: R${novo_salario:.2f}')
