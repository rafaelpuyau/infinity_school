'''
Faça um programa que imprima 50 números (de 0 à 50 inclusive) pulando de 5 em 5.
'''

# Função Range com:
# Início em 0
# Fim com 51 (esse valor não é incluído no iterável)
# Passo ou saldo de 5
for numero in range(0, 51, 5):
    print(numero, end=' ')
