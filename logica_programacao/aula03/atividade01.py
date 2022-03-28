'''
Guardar um número sorteado entre 1 e 10 e pedir para que o usuário tente acertar este valor. Avise a ele se o número que ele informou é maior ou menor do número sorteado e mostre a mensagem quando ele acertar!
Faça antes do código um fluxograma para estruturar melhor o raciocínio
'''

# Importação da função randrange do módulo random
from random import randrange

# Atribuição de um número aleatório à variável numero_sorteado
numero_sorteado = randrange(1, 10)

# Condição sempre verdadeira para o laço while
while True:
    # Solicito um número ao usuário através da entrada de teclado e faço o casting para inteiro
    palpite_usuario = int(input('Qual foi o número sorteado? '))
    # Verifico se o palpite do usuário é igual ao número sorteado
    if palpite_usuario == numero_sorteado:
        print('PARABÉNS! Você acertou.')
        print(f'O número sorteado foi {numero_sorteado}')
        # Interrupção do laço infinito, ou seja, saimos do laço while
        break
    # Caso o palpite não seja igual ao número sorteado
    else:
        # Verifico se o palpite é maior que o número sorteado e informo ao usuário
        if palpite_usuario > numero_sorteado:
            print(f'Seu palpite ({palpite_usuario}) é maior que o número sorteado')
        # Verifico se o palpite é menr que o número sorteado e informo ao usuário
        elif palpite_usuario < numero_sorteado:
            print(f'Seu palpite ({palpite_usuario}) é menor que o número sorteado')
        print('TENTE NOVAMENTE')
        

        