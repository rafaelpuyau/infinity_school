'''
Faça um programa que mostre na tela a seguinte contagem: 0 3 6 9 12 15 18 Acabou!
'''

# Início em 0
# Fim em 19 (não incluído no iterável)
# Passo definido como 3
for numero in range(0, 19, 3):
    # end=' ' para que os números fiquem lado a lado
    print(numero, end=' ')

print('Acabou!')