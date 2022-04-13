'''
Faça um programa que leia o peso e a altura de 7 pessoas, mostrando no final:

    Qual foi a média de altura do grupo
    Quantas pessoas pesam mais de 90kg
    Quantas pessoas que pesam menos de 50kg tem menos de 1.60m
    Quantas pessoas que medem mais de 1.90m pesam mais de 100kg
'''

# Inicialização das variáveis
somatorio_altura = 0
media_altura_grupo = 0 
pesam_mais_90 = 0
pessoas_menos_50_160 = 0
pessoas_mais_100_190 = 0

for passo in range(1, 8):
    # Leio os dados do peso e altura das 7 pessoas
    peso = float(input(f'Entre com o peso da {passo}ª pessoa: '))
    altura = float(input(f'Entre com a altura da {passo}ª pessoa: '))
    
    somatorio_altura += altura
    # Bloco condicional para testar os valores e popular as variáveis
    if peso > 90:
        pesam_mais_90 += 1
    elif peso < 50 and altura < 1.60:
        pessoas_menos_50_160 += 1
    elif peso > 100 and altura > 1.90:
        pessoas_mais_100_190 += 1
        
# Cálculo da média da altura do grupo        
media_altura_grupo = somatorio_altura / 7

# Exibo as informações na tela
# A média da altura do grupo está formatada com 2 casas decimais
print(f'A média da altura do grupo é de {media_altura_grupo:.2f}m')
print(f'{pesam_mais_90} pessoas pesam mais que 90kg')
print(f'{pessoas_menos_50_160} pessoas pesam menos de 50kg e medem menos de 1.60m')
print(f'{pessoas_mais_100_190} pessoas pesam mais de 100kg e medem acima de 1.90m')
