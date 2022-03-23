'''
Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: 
1) Ter no mínimo 65 anos de idade. 
2) Ter trabalhado no mínimo 30 anos. 
3) Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos. 
Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho do
empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'
'''

from datetime import datetime as dt

# Leio os dados do empregado
codigo = int(input('Código do empregado: '))
ano_nascimento = int(input('Ano de nascimento [AAAA]: '))
ano = int(input('Ano de ingresso na empresa: '))

# Escrevo na tela as informações solicitadas
# Calculo a idade. Outra forma de fazer seria 2022 - ano_nascimento
idade = dt.today().year - ano_nascimento
print(f'O empregado tem {idade} anos')

# Calculo o tempo de trabalho
tempo_trab = dt.today().year - ano
print(f'O empregado trabalha há {tempo_trab} anos na empresa')

# Verifico as condições
if idade >= 60 and tempo_trab >= 25:
    print('Requerer aposentadoria')
elif idade >= 65 or tempo_trab >= 30:
    print('Requerer aposentadoria')
else:
    print('Não requerer')
    