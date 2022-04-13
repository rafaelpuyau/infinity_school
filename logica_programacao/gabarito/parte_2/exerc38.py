'''
O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.
'''

# Inicializo as variáveis
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

# Verifico se o início é maior que o fim
# Se for, a contagem será regressiva
# Inverto o sinal do passo
if inicio > fim:
    passo *= -1

# Executo a contagem
for numero in range(inicio, fim, passo):
    print(numero, end=' ')
    
print('Fim da contagem!')
