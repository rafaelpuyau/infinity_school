'''
Faça um programa que mostre uma contagem regressiva de 30 até 1, marcando os números que forem divisíveis por 4, exatamente como mostrado a seguir: 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...
'''

# Início em 30
# Fim em 0 pois queremos imprimir até o 1
# Passo em -1 para que haja contagem regressiva
for numero in range(30, 0, -1):
    # Verifico se o número é divisível por 4 e aplico o filtro caso seja verdadeiro
    if numero % 4 == 0:
        print(f'[{numero}]', end=' ')
    else:
        print(numero, end=' ')
