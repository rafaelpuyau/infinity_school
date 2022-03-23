'''
Escreva um algoritmo para ler as dimensões de um retângulo (base e altura),
calcular e escrever a área do retângulo (base * altura)
'''

# Imprimo um título na tela e coloco em maiúsculas
print('área do retângulo'.upper())

# Solicito os dados do usuário
base = float(input('Informe a base: '))
altura = float(input('Informe a altura: '))

# Aplico a fórmula para o cálculo da área do retângulo
area = base * altura

# Imprimo a área na tela e formato a saída para 2 casas decimais

# f-string
print(f'A área do retângulo é de {area:.2f}')

# Com o método format()
print('A área do retângulo é de {0:.2f}'.format(area))
