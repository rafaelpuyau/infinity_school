'''
Uma empresa de exportação de Eletrodos vende contêineres com valores fixos por toneladas. Um caminhão pode sair com várias toneladas e foi preciso desenvolver um sistema para calcular o valor mensal faturado. 
Desenvolva este sistema que irá solicitar o valor fixo da tonelada no início do programa e peça para o usuário quantas vezes forem necessárias a quantidade de toneladas que saiu (cada mês pode sair quantidade diferente). Ao final, mostre o valor total faturado
'''

# ATENÇÃO : para essa atividade estamos considerando um período fixo de 12 meses

# Inicialização da variável total_faturado com o valor zero
total_faturado = 0

# Solicita a entrada de dados do usuário. Realizamos o casting para float
valor_tonelada = float(input('Valor da Tonelada [R$]: '))

# Laço for com a função range que gera uma estrutura iterável com 12 elementos
# O range está iniciando em 1 (inclui esse valor) e terminando no 13 (exclui esse valor)
# Logo, o iterável vai de 1 à 12, representando os meses do ano
for mes in range(1, 13):
    # Solicita a entrada de dados do usuário. Realizamos o casting para int
    quantidade_tonelada = int(input(f'Quantidade de tonelada para o mês {mes}: '))
    # Calculamos o custo do mês multiplicando a quantidade pelo valor da tonelada e depois
    # somamos ao total_faturado
    total_faturado += valor_tonelada * quantidade_tonelada

# Saída na tela do total faturado
print(f'O valor total faturado foi de R${total_faturado:.2f}')
