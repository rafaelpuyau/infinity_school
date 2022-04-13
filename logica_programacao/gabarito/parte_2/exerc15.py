'''
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada km acima da velocidade permitida.
'''

velocidade_carro = int(input('Velocidade do carro [km/h]: '))

if velocidade_carro > 80:
    # Cálculo da multa
    multa = (velocidade_carro - 80) * 5
    print(f'Você foi multado no valor de R${multa:.2f}')
else:
    print('Você dirigiu dentro dos limites de velocidade permitidos')
