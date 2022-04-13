'''
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar. Considere pessoas com idade igual ou superior a 18 anos como voto obrigatório, entre 16 e 18 (maior ou igual a 16 e menor que 18) como voto facultativo, maiores de 60 anos como facultativo também e menores de 16 anos não tem idade para votar.
'''

# Importo a biblioteca datetime para pegar o ano atual automaticamente do sistema
from datetime import datetime as dt

ano_nascimento = int(input('Ano de Nascimento: '))

# Pego o ano atual 
ano_atual = dt.today().year

# Calculo a idade
idade = ano_atual - ano_nascimento

# Verifico onde a idade se enquadra no bloco condicional e exibo a mensagem na tela
if idade > 60:
    print('Voto facultativo')
elif idade >= 18:
    print('Voto obrigatório')
elif idade >= 16:
    print('Voto facultativo')
else:
    print('Não tem idade para votar')
