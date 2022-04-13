'''
Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:

    Quantos homens foram cadastrados
    Quantas mulheres foram cadastradas
    A média da idade do grupo
    A média da idade dos homens
    Quantas mulheres tem mais de 20 anos
'''

# Inicialização das variáveis
homens = 0
mulheres = 0
somatorio_idade = 0
media_idade_homens = 0
mulheres_20 = 0

# Laço for com a função range iniciando em 1 e terminando em 5, 6 não é incluído neste iterável
for i in range(1, 6):
    print(f'Lendo os dados da {i}ª pessoa...')
    idade = int(input('Idade: '))
    sexo = input('Sexo [masculino / feminino]: ')
    
    somatorio_idade += idade
    
    # Normalizo a entrada do usuário na variavel sexo colocando toda a string em minúsculas
    if sexo.lower() == 'masculino':
        homens += 1
        media_idade_homens += idade
    elif sexo.lower() == 'feminino':
        mulheres += 1
        if idade > 20:
            mulheres_20 += 1

# Cálculo das médias do grupo e dos homens
media_grupo = somatorio_idade / 5
media_idade_homens = media_idade_homens / homens


# Exibição na tela das informações solicitadas
print(f'{homens} homens cadastrados')
print(f'{mulheres} mulheres cadastradas')
print(f'{media_grupo} é a média da idade do grupo')
print(f'{media_idade_homens} está é a média da idade dos homens')
print(f'{mulheres_20} mulheres tem mais de 20 anos')
