'''
Faça um programa que imprima 20 números (de 0 à 19) em ordem decrescente e um do lado do outro.
'''

# Para imprimir na ordem decrescente, a função Range
# teve o start com 19, o end com -1, pois queremos imprimir
# o 0 e o passo foi de -1 para que haja o decréscimo dos números
for numero in range(19, -1, -1):
    print(numero, end=' ')