'''
Faça um programa usando a estrutura FOR que mostre na tela a seguinte sequência: 100 90 80 70 60 50 40 30 20 10 0 Acabou
'''

# Início em 100
# Fim em -1 para que o 0 seja incluído no iterável
# Passo negativo em -10 para contagem regressiva
for numeros in range(100, -1, -10):
    print(numeros, end=' ') # Parâmetro end com espaço para que saiam lado a lado
    
print('Acabou')