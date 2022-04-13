'''
Um programa de vida saudável quer dar pontos por atividades físicas que podem ser trocados por dinheiro. O sistema funciona assim:
    Cada hora de atividade física no mês vale pontos:
        Até 10h de atividade no mês: ganha 2 pontos por hora
        De 10h até 20h de atividade no mês: ganha 5 pontos por hora
        Acima de 20h de atividade no mês: ganha 10 pontos por hora
    A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)

Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve e quanto quanto dinheiro ela conseguiu ganhar.
'''

# Constante do valor do ponto
VALOR_PONTO = 0.05

# Leio quantas horas de atividade o usuário realizou no mês
horas_atividades = int(input('Quantas horas de atividade física você fez este mês? '))

# De acordo com a quantidade de horas, calculo o ganho de pontos
if horas_atividades > 20:
    pontos_ganhos = horas_atividades * 10
elif horas_atividades < 10:
    pontos_ganhos = horas_atividades * 2
else:
    pontos_ganhos = horas_atividades * 5

# Conversão dos pontos em dinheiro
pontos_em_dinheiro = pontos_ganhos * VALOR_PONTO

# Exibo na tela as informações
print(f'Você acumulou {pontos_ganhos} pontos')
# Formato em 2 casas decimais o dinheiro ganho pelo cliente
print(f'E ganhou R${pontos_em_dinheiro:.2f}')
