'''
Faça um programa que leia o nome, a idade e o sexo de vários pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final deverá mostrar em tela:

    O nome da pessoa mais velha
    O nome da mulher mais jovem
    A média da idade do grupo
    Quantos homens tem mais de 30 anos
    Quantas mulheres tem menos de 18 anos
'''

# Inicialização das variáveis
mais_velha = 0
mais_jovem = None
nome_mais_velha = ''
mulher_mais_jovem = ''
somatorio_idade = 0
tamanho_grupo = 0
homens_30 = 0
mulheres_18 = 0

while True:
    # Uso a função title() para colocar a primeira letra do nome em maiúscula.
    # Isso vale, também, para nomes compostos
    nome = input('Nome: ').title()
    idade = int(input('Idade: '))
    # Normalizo a entrada do usuário colocando a string em minúsculas e pegando a 1ª letra que está no índice 0
    sexo = input('Sexo: ').lower()[0]
    
    # Testo se a idade é maior que o valor em mais_velha.
    # Se sim, pego o nome salavando em nome_mais_velha e atribuo essa idade à mais_velha
    if idade > mais_velha:
        mais_velha = idade
        nome_mais_velha = nome
    
    # Primeiro verifico se é mulher
    if sexo == 'f':
        # Depois se o valor de mais_jovem é None. Significa que está rodando pela 1ª vez
        if mais_jovem == None:
            mais_jovem = idade # Atribuo a idade lida à mais_jovem
        elif idade < mais_jovem:
            mulher_mais_jovem = nome
    
    # Conto os homens com mais de 30 anos
    if sexo == 'm' and idade > 30:
        homens_30 += 1
    # Conto as mulheres com menos de 18 anos
    elif sexo == 'f' and idade < 18:
        mulheres_18 += 1
    
    somatorio_idade += idade
    tamanho_grupo += 1    
    
    continuar = input('Deseja continuar? [S/N] ').lower()[0]
    
    # Saio do laço se contiuar receber n
    if continuar == 'n':
        break

# Cálculo da média de idade
media_idade = somatorio_idade / tamanho_grupo

# Exibo as informações
print(f'{nome_mais_velha} é a pessoa mais velha')
print(f'{mulher_mais_jovem} é a mulher mais jovem')
print(f'{media_idade} é a média da idade deste grupo')
print(f'{homens_30} homens tem mais de 30 anos')
print(f'{mulheres_18} mulheres tem menos de 18 anos')
