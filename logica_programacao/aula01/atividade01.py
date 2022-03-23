'''
Faça um algoritmo para calcular o IMC do usuário

Fórmula : IMC = peso / altura * altura

IMC                 CLASSIFICAÇÃO
< 18.5              Peso Baixo / Muito magro
18.5 - 24.9         Peso Normal
25.0 - 29.9         Sobrepeso
30.0 - 34.9         Obesidade (Grau I)
35.0 - 39.9         Obesidade (Grau II)
>= 40               Obesidade Mórbida (Grau III)
'''

# Solicito os dados do usuário
# Transformo o retorno da função input, que é uma string, em um número float
# através do casting com a função float()
peso = float(input('Informe seu peso [kg]: '))
altura = float(input('Informe sua altura [m]: '))

# Faço o cálculo do IMC
imc = peso / (altura * altura)

# Imprimo na tela o resultado do IMC

# Utilizando a f-string
print(f'Seu IMC é de {imc:.2f}')

# Utilizando o método format()
print('Seu IMC é de {0:.2f}'.format(imc))

# Utilizando a concatenação de strings e casting
# Não se preocupe agora com essa sintaxe aplicada após o casting. 
# Veremos mais pra frente o slice
print('Seu IMC é de ' + str(imc)[:5])

