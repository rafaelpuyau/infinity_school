'''
Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:

    Homens ganham 5% de desconto
    Mulheres ganham 15% de desconto
'''

# Solicito os dados ao usuário
nome = input('Nome: ')
sexo = input('Sexo: ')
# Casting para float por se tratar de valor monetário
valor_compras = float(input('Valor das compras [R$]: '))

# Verifico se é do sexo feminino. Sendo verdade, aplico os 15% 
# Para facilitar a conta, multiplicar por 0.85 é equivalente que dar 5% de desconto e somar com o valor das compras
if sexo == 'feminino':
    valor_compras *= 0.85
    # Formato o valor das compras com 2 casas decimais
    print(f'{nome} ganhou 15% de desconto e pagará R${valor_compras:.2f}')
else:
    # Vale a mesma explicação para o sexo feminino. So que aqui aplicamos o percentual para o sexo masculino
    valor_compras *= 0.95
    # Formato o valor das compraas com 2 casas decimais
    print(f'{nome} ganhou 5% de desconto e pagará R${valor_compras:.2f}')
