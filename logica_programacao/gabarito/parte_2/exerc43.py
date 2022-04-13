'''
Faça um programa que faça o sorteio de 10 números entre 0 e 10 (inclusive) e mostre na tela:

    Quais foram os números sorteados
    Quantos números estão acima de 5
    Quantos números são divisíveis por 3
'''

# Importo da biblioteca random, a função randint que inclui o intevalo de 0 e 10, inlcuindo eles mesmos
from random import randint

# Inicializo as variáveis que irão contar 
# os números acima de 5 e os divisíveis por 3
acima_5 = 0
divisiveis_3 = 0

print('Nºs sorteados:', end=' ')

# Faço o sorteio dos 10 números e testo quais são acima de 5 e divisíveis por 3
for num in range(10):
    numero = randint(0, 10)
    print(numero, end=' ')
    # Se o número for divisível por 3 e maior que 5, somo 1 as variáveis de contagem
    # o comando continue força o programa ir para a próxima iteração
    if numero % 3 == 0 and numero > 5:
        divisiveis_3 += 1
        acima_5 += 1
        continue
    elif numero > 5:
        acima_5 += 1
    # 0 % 3 == 0 logo só posso somar se número for diferente de 0 e divisível por 3
    elif numero % 3 == 0 and numero != 0:
        divisiveis_3 += 1

# Exibo as mensagens na tela
print(f'\n{acima_5} estão acima de 5')
print(f'{divisiveis_3} são divisíveis por 3')
