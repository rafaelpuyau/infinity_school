'''
[ DESAFIO ] Faça um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível formar um triângulo com essas retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.
'''

# Leio os 3 segmentos de reta
seg_reta_1 = int(input('Tamanho da reta 1: '))
seg_reta_2 = int(input('Tamanho da reta 2: '))
seg_reta_3 = int(input('Tamanho da reta 3: '))

# Testo para saber se podem formar um triângulo, atribuindo um valor booleano as variáveis lados
lado_1 = seg_reta_1 < seg_reta_2 + seg_reta_3
lado_2 = seg_reta_2 < seg_reta_1 + seg_reta_3
lado_3 = seg_reta_3 < seg_reta_1 + seg_reta_2

# Se os três lados forem TRUE, esse if é verdadeiro e exibo na tela que podem formar um triângulo
if lado_1 and lado_2 and lado_3:
    print('Pode formar um triângulo')
else:
    # Só exibo na tela essa mensagem se pelo um dos lados receber FALSE
    print('Não podem formar um triângulo')
