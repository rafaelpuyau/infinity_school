'''
Faça um programa que leia o sexo e peso de 8 pessoas, usando a estrutura FOR. No final, mostre na tela:

    Quantas mulheres foram cadastradas
    Quantos homens pesam mais de 100kg
    A média de peso entre as mulheres
    O maior peso entre os homens
'''

# Inicialização das variáveis
mulheres = 0
homens_100 = 0
somatorio_peso_mulheres = 0
maior_peso_homens = 0

# Laço for com repeitção de 8x
# A função range cria um iterável de 0 à 7
for x in range(8):
    # Pego somente a 1ª letra do sexo informado pelo usuário
    sexo = input('Sexo: ').lower()[0]
    peso = float(input('Peso: '))
    
    if sexo == 'f':
        mulheres += 1
        somatorio_peso_mulheres += peso
    elif sexo == 'm':
        # Testo se o peso informado é maior que o maior peso já registrado e testo, também se peso é maior que 100
        if peso > maior_peso_homens and peso > 100:
            maior_peso_homens = peso
            homens_100 += 1
        # Testo apenas se é maior que 100, pois aqui peso pode ser maior que 100 e não ser maior que o maior peso registrado
        elif peso > 100:
            homens_100 += 1
        # Caso nenhum peso acima de 100 seja lido, testo se o peso é maior que o maior peso registrado
        elif peso > maior_peso_homens:
            maior_peso_homens = peso
       
# Calculo a média do peso das mulheres
media_peso_mulheres = somatorio_peso_mulheres / mulheres
 
# Exibo as informações na tela
# Formato as variáveis float com 2 casas decimais
print(f'{mulheres} mulheres foram cadastradas')
print(f'{homens_100} homens pesam mais de 100kg')
print(f'A média de peso entre as mulheres é de {media_peso_mulheres:.2f}kg')
print(f'E o maior peso entre os homens foi {maior_peso_homens:.2f}kg')
