'''
Faça um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou! OBS: Contagem regressiva de 100 até 0 pulando de 5 em 5.
'''

# Início em 100
# Fim em -1 pois queremos imprimir o 0 (-1 não será incluído no iterável)
# Passo em -5 para que a contagem seja regressiva de 5 em 5
for numero in range(100, -1, -5):
    print(numero, end=' ')

print('Acabou!')
