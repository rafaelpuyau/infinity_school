'''
Crie um programa que leia o nome e o salário de um funcionário, mostrando na tela a seguinte mensagem: O funcionário Rafael tem um salário de R$5000.00.
'''

# Recebo o nome do funcionário
nome_func = input('Nome do funcionário: ')
# Recebo o salário e faço o casting para float
salario_func = float(input('Salário do funcionário [R$]: '))

# Imprimo na tela o nome do funcionário com o método capitalize
# para colocar a primeira letra em maiúscula
# Formato o salário com 2 casas decimais
print(f'O funcionário {nome_func.capitalize()} tem um salário de R${salario_func:.2f}')
