'''
Faça um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a ler a próxima pessoa. No final, mostre em tela:

    Qual é a maior idade lida
    Quantos homens foram cadastrados
    Qual é a idade da mulher mais jovem
    Qual é a média da idade entre os homens
'''

# Inicialização das variáveis
maior_idade = 0 
homens_cadastrados = 0 
idade_mulher_jovem = None # Inicializei como vazio para capturar o primeiro valor
somatorio_homens = 0


while True:
    # Coloco a string em minúsculas e pego somente a primeira letra que está no índice 0
    sexo = input('Sexo: ').lower()[0]
    idade = int(input('Idade: '))
    
    if idade > maior_idade:
        maior_idade = idade 
    
    if sexo == 'm':
        homens_cadastrados += 1
        somatorio_homens += idade
    elif sexo == 'f':
        # Verifico se a variável idade_mulher_jovem está vazia e coloco a primeira idade lida nela
        if idade_mulher_jovem == None:
            idade_mulher_jovem = idade
        elif idade < idade_mulher_jovem:
            idade_mulher_jovem = idade
    
    # Pego somente a primeira letra da resposta do usuário se quer continuar ou não
    continuar = input('Quer continuar? [S/N] ').lower()[0]
    
    # Faço a comparação nesse bloco condicional e se for igual a n, uso o break para sair do laço
    if continuar == 'n':
        break

# Cálculo da média da idade dos homens
media_idade_homens = somatorio_homens / homens_cadastrados

# Exibo na tela as informações solicitadas
print(f'Maior idade lida: {maior_idade}')
print(f'{homens_cadastrados} homens cadastrados')
print(f'{idade_mulher_jovem} anos é a idade da mulher mais jovem')
print(f'Média de idade entre os homens: {media_idade_homens}')
