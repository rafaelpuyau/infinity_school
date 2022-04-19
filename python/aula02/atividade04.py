'''
Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome.
'''

def media_aluno(notas):
    '''
        Esta função calcula a média de um aluno previamente cadastrado no dicionário
        
        params:
            notas -> list : notas do aluno
        
        return:
            media -> float : media aritimética
    '''
    media = sum(notas) / len(notas)
    return media
    

alunos = dict()

while True:
    notas = list()
    nome_aluno = input('Nome do aluno: ').title()
    if nome_aluno == '':
        break
    else:
        print(f'Lendo as notas de {nome_aluno}...')
        for nota in range(1, 3):
            notas.append(float(input(f'Entre com a {nota}ª nota: ')))
        alunos[nome_aluno] = notas


nome_aluno = input('Deseja calcular a média de qual aluno? ').title()

if nome_aluno in alunos.keys():
    print(f'A media do aluno {nome_aluno} é {media_aluno(alunos[nome_aluno]):.2f}')
else:
    print('Aluno não encontrado no cadastro')
