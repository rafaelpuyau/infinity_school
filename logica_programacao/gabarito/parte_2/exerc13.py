'''
Faça um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$35 por hora trabalhada.
'''

# Constantes
HORAS_POR_DIA = 8
VALOR_HORA = 35

# Leio os dias trabalhados e faço o casting para int
dias_trabalhados = int(input('Nº de dias trabalhados: '))

# Cálculo do salário
salario = dias_trabalhados * HORAS_POR_DIA * VALOR_HORA

# Imprimo na tela o salário calculado com base no dias trabalhados e formatando a saída 
# com 2 casas decimais
print(f'O salário do funcionário é R${salario:.2f}')
