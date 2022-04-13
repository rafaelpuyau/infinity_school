'''
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.

    Se estiver antes dos 18 anos, mostrar quantos anos faltam para o alistamento
    Se já tiver acima dos 18 anos, mostrar quantos anos já se passaram do alistamento
'''

# Importação da biblioteca datetime
from datetime import datetime as dt

# Leio o ano de nascimento do usuário
ano_nascimento = int(input('Ano de Nascimento: '))

# Calculo a idade
idade = dt.today().year - ano_nascimento

# Verifico se a idade é maior ou menor que 18
if idade < 18:
    # Faço a conta dentro dos parentesis na f-string sem a necessidade de armazenar numa variável
    print(f'Faltam {18 - idade} anos para o alistamento')
else:
    print(f'Já se passaram {idade - 18} anos do alistamento')
