'''
[ SUPER DESAFIO ] Crie um jogo de JokenPo (Pedra, papel, tesoura) ATENÇÃO: utlize o método shuffle para embaralhar os valores dentro de uma lista em python e pegue o primeiro elemento dessa lista. (Ex. from random import shuffle)
'''

# Importo do módulo Random a função shuffle
from random import shuffle

# Carrego as opções do computador
computador = ['pedra', 'papel', 'tesoura']
# Embaralho as opções
shuffle(computador)

# Solicito a opção do jogador
jogador = input('Pedra, Papel ou Tesoura? ')

# Apenas mostro as opções para me certificar 
# print(f'Jogada Computador: {computador[0].lower()}')
# print(f'Jogada do Usuário: {jogador.lower()}')


# Testo as opções e vejo quem ganhou
if jogador == computador[0]:
    print('EMPATOU')
else:
    if jogador.lower() == 'pedra' and computador[0].lower() == 'tesoura':
        print('VOCÊ GANHOU!')
    elif jogador.lower() == 'pedra' and computador[0].lower() == 'papel':
        print('COMPUTADOR GANHOU!')
    elif jogador.lower() == 'papel' and computador[0].lower() == 'pedra':
        print('VOCÊ GANHOU!')
    elif jogador.lower() == 'papel' and computador[0].lower() == 'tesoura':
        print('COMPUTADOR GANHOU!')
    elif jogador.lower() == 'tesoura' and computador[0].lower() == 'papel':
        print('VOCÊ GANHOU!')
    elif jogador.lower() == 'tesoura' and computador[0].lower() == 'pedra':
        print('COMPUTADOR GANHOU!')
