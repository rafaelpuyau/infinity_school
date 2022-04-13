'''
Faça um programa que mostre na tela a soma dos números de 500 a 0 pulando de 50 em 50. Ex.: 500 + 450 + 400 + 350 + 300 + ... + 50 + 0.
'''

# Inicializo a variável em 0
somatorio = 0

# A função range cria o iterável iniciando em 500, indo até 0 (-1 não é incluído no iterável)
# e o passo -50 para contagem regressiva
for numero in range(500, -1, -50):
    somatorio += numero
    
# Exibo o somatório na tela
print(f'Somatório: {somatorio}')
