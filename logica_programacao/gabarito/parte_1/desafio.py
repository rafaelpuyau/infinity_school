'''
[ DESAFIO ] : Refaça o programa de advinhação onde o computador sortea um número e o usuário tenta adivinhá-lo. Dessa vez, o usuário terá 5 tentativas. A cada tentativa errada, informe se o palpite do usuário é menor ou maior que o número sorteado. Se ele errar as 5 tentativas, o programa deve imprimir "Você errou!" e mostrar qual era o número sorteado. Caso ele acerte, mostre a mensagem "Você acertou!" e e qual tentativa ele acertou o número sorteado.
'''

from random import randrange

numero_sorteado = randrange(1, 11)

for tentativa in range(1, 6):
    print(f'TENTATIVA nº{tentativa}')
    palpite = int(input('Palpite [1 à 10]: '))
    
    if palpite == numero_sorteado:
        print(f'PARABÉNS! Você acertou na {tentativa}º tentativa!')
        break
    else:
        if tentativa == 5:
            print('Você errou!')
            print(f'O número sorteado era {numero_sorteado}')
            break
        elif palpite > numero_sorteado:
            print('Seu palpite é maior que o número sorteado')
        elif palpite < numero_sorteado:
            print('Seu palpite é menor que o número sorteado')
