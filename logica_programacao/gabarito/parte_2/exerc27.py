'''
Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''

# Leio os dados
valor_casa = float(input('Valor da casa [R$]: '))
salario_comprador = float(input('Salário do comprador [R$]: '))
anos_pagar = int(input('Em quantos anos o comprador deseja pagar? '))

# Calculo o valor da prestação
valor_prestacao = valor_casa / (anos_pagar * 12)

# Calculo 30% do salário do comprador
salario_30 = salario_comprador * 0.30

# Vejo se o valor da prestação é menor ou não que 30% do salário do comprador e exibo a mensagem adequada
if valor_prestacao <= salario_30:
    print('Empréstimo concedido')
else:
    print('Empréstimo negado')
