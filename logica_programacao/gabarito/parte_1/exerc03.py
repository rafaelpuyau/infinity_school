'''
Faça um programa que leia o salário e o valor da prestação. Se a prestação for maior que 20% do salário lido, imprimir a mensagem: Empréstimo não pode ser concedido. Senão imprimir: Empréstimo concedido.
'''

# Leitura dos dados solicitados

# Casting para float pois salário é um número com casa decimal
salario = float(input('Salário [R$]: '))

# Casting para float pois a prestação, também, é um número 
# com casa decimal
valor_prestacao = float(input('Valor da Prestação [R$]: '))

# Verifico se a prestação é maior que 20% do salário
# Calculo 20% do salário lido
percent_20 = salario * 0.20

# Agora verifico se o valor da prestação é maior que 20% do
# salário
if valor_prestacao > percent_20:
    print('Empréstimo não pode ser concedido')
else:
    print('Empréstimo concedido')
