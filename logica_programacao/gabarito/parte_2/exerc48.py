'''
Faça um programa que leia vários números pelo teclado e mostre no final o somatório entre eles. O programa será interrompido quando o número 9999 for digitado. OBS: Esse valor de 9999 não deve entrar no somatório
'''

# Inicializo a variável que receberá a soma dos números
somatorio = 0

# Laço while com condição sempre em True
while True:
    numero = int(input('Número: '))
    
    # Antes de somar, verifico se o número lido é 9999 e saio do laço sem somá-lo
    if numero == 9999:
        break
    
    somatorio += numero

# Exibo na tela o somatório deles
print(f'Somatório dos números lidos: {somatorio}')
