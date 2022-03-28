'''
Criar um algoritmo para mostrar quantas vogais tem em uma palavra digitada
'''

# Inicializo a variável vogais com zero. Ela é a responsável por armazenar quantas vogais 
# a palavra digitada possui
vogais = 0

# Solicita que o usuário digite uma palavra
palavra_digitada = input('Palavra: ')

# Laço FOR para iterar sobre a palavra digitada
for vogal in palavra_digitada:
    # Forma mais otimizada de verificar se a vogal ou caracter é uma das vogais
    # Lembre-se que CASE SENTIVE diferencia os valores, por isso repetimos as vogais em 
    # minúsculas e maiúsculas
    if vogal in 'aeiouAEIOU':
        vogais += 1

# Exibo na tela a quantidade de vogais da palavra digitada
print(f'A palavra {palavra_digitada} tem {vogais} vogais')
