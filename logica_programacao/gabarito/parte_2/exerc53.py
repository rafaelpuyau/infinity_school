'''
Faça um programa usando a estrutura FOR que mostre na tela a seguinte sequência: 0 5 10 15 20 25 30 35 40 Fim
'''

# Início em 0 (inluído)
# Fim em 41 (excluído)
# Passo em 5 para saltar de 5 em 5 
for numeros in range(0, 41, 5):
    print(numeros, end=' ') # parâmetro end com espaço para que os números saiam lado a lado

print('Fim')  
