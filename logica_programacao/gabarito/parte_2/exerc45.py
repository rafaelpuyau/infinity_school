'''
Faça um programa que leia a idade de 10 pessoas, mostrando no final:

    Qual é a média de idade do grupo
    Quantas pessoas tem mais de 18 anos
    Quantas pessoas tem menos de 18 anos
    Qual foi a maior idade lida
'''

# Inicializo as variáveis
maior = 0
menos_18 = 0
mais_18 = 0
somatorio_idades = 0

# Função range iniciando em 1 e terminando em 10, pois o 11 não é incluído neste iterável
for i in range(1, 11):
    idade = int(input(f'Idade da {i}ª pessoa: '))
    somatorio_idades += idade
    # Bloco condicional onde testo as possibilidades de acordo com o descrito acima
    if idade > 18:
        mais_18 += 1
    elif idade < 18:
        menos_18 += 1
    
    if idade > maior:
        maior = idade

# Cálculo da média
media = somatorio_idades / 10

# Exibo na tela
print(f'A média das idades do grupo é de {round(media)} anos')
print(f'{mais_18} pessoas tem mais de 18 anos')
print(f'{menos_18} pessoas tem menos de 18 anos')
print(f'A maior idade lida foi {maior}')
