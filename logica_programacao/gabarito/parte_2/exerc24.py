'''
Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:

    Abaixo de 100m² = TERRENO POPULAR
    Entre 100m² e 500m² = TERRENO MASTER
    Acima de 500m² = TERRENO VIP
'''

# Leio a largura e o comprimento
largura = float(input('Largura [m²]: '))
comprimento = float(input('Comprimento [m²]: '))

# Calculo a área 
area = largura * comprimento

# Verifico a área em m² e classifico o terreno de acordo com o tamanho do mesmo
if area > 500:
    print('TERRENO VIP')
elif area > 100:
    print('TERRENO MASTER')
else:
    print('TERRENO POPULAR')
