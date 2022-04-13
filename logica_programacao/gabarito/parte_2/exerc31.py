'''
Escreva um programa que mostre na tela a seguinte contagem: 6 7 8 9 10 11 Acabou!
'''

# Laço for com a função range iniciando em 6 e terminando em 12 pois queremos imprimir o número 11
# Lembre-se que o valor final desta função não é incluído
for numero in range(6, 12):
    # Por padrão o print tem um \n no parâmetro end. Como queremos lado a lado basta informar um espaço
    print(numero, end=' ')

print('Acabou!')
