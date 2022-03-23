'''
A cancela de um estabelecimento, neste momento de pandemia funciona dependendo da temperatura aferida e registrada pelo recepcionista do local. É preciso criar um algoritmo para liberar ou não cancela dependendo da temperatura corporal. Com um medidor o recepcionista irá aferir e registrar no sistema e o algoritmo deverá liberar caso a temperatura seja <= 37 e não liberar caso a temperatura seja maior que 37º.
A cancela só recebe True ou False (True para liberar e False para bloquear)
'''

# Inicializo a variável referente a cancela como False
liberarCancela = False

# Faço a leitura da temperatura
temperatura = float(input('Temperatura aferida [ºC]: '))

# Testo se a temperatura é menor ou igual a 37ºC
if temperatura <= 37:
    liberarCancela = True
    
# Apenas imprimo na tela o conteúdo da cancela
print(liberarCancela)
