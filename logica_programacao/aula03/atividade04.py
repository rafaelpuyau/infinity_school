'''
Um instituto de pesquisa entre portadores de COVID-19 selecionou uma amostra de 10 pacientes em uma região no  intuito de saber a porcentagem de:
Pacientes com sintomas leves da doença;
Pacientes assintomáticos;
Pacientes com sintomas graves da doença.
Ao final, o intuito é obter uma porcentagem de cada uma das classificações acima. Crie um algoritmo para auxiliar o instituto a registrar e calcular este percentual
'''

# Inicializo as 3 variáveis com 0
sin_leves = assin = sin_graves = 0

# Laço FOR percorrendo a amostra de 10 pacientes
# Lembre-se: o range inclui o primeiro valor e exclui o segundo
for paciente in range(1, 11):
    # Utilização das aspas triplas para formar um menu e casting para inteiro
    print(f'''
    O paciente {paciente} apresentou:
        1 - Sintomas leves
        2 - Assintomáticos
        3 - Sintomas graves''')
    amostra = int(input('Amostra: '))
    
    # Verifico o valor de entrada do usuário
    if amostra == 1:
        sin_leves += 1
    elif amostra == 2:
        assin += 1
    else:
        sin_graves += 1
    
# Já fora do laço FOR, faço os cálculos dos percentuais
sin_leves = sin_leves / 10 * 100
assin = assin / 10 * 100
sin_graves = sin_graves / 10 * 100

# Exibição na tela dos percentuais com uma casa decimal
print(f'{sin_leves:.1f}% dos pacientes com sintomas leves')
print(f'{assin:.1f}% dos pacientes assintomáticos')
print(f'{sin_graves:.1f}% dos pacientes com sintomas graves')
