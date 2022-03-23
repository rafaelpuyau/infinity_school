'''
A Secretaria de Meio Ambiente que controla o índice de poluição mantém 3 grupos de indústrias que são altamente poluentes do meio ambiente. O índice de poluição aceitável varia de 0,05 até 0,25. Se o índice sobe para 0,3 as indústrias do 1º grupo são intimadas a suspenderem suas atividades, se o índice crescer para 0,4 as indústrias do 1º e 2º grupo são intimadas a suspenderem suas atividades, se o índice atingir 0,5 todos os grupos devem ser notificados a paralisarem suas atividades. Faça um algoritmo que leia o
índice de poluição medido e emita a notificação adequada aos diferentes grupos de empresas
'''

# Leio o índice de poluição
indice_poluicao = float(input('Índice de Poluição: '))

# Verifico se o índice lido está dentro do intervalo de 0.05 até 0.25
if 0.05 <= indice_poluicao <= 0.25:
    print('Índice de poluição aceitável')
elif indice_poluicao >= 0.5:
    print('As indústrias de todos os grupos serão intimadas a suspenderem suas atividades')
elif indice_poluicao >= 0.4:
    print('As indústrias do 1º e 2º grupos serão intimadas a suspenderem suas atividades')
elif indice_poluicao >= 0.3:
    print('As indústrias do 1º grupo serão intimadas a suspenderem suas atividades')
else:
    print('Índice de poluição fora dos limites, favor repetir a leitua')
