'''
Faça um programa que leia a idade de vários alunos de uma turma. O programa vai parar quando for digitada a idade 999. No final, mostre quantos alunos existem na turma e qual é a média de idade do grupo.
'''

# Inicialização das variáveis
total_alunos = 0
somatorio_idade = 0

while True:
    idade = int(input('Idade do aluno: '))
    
    # Condicional que verifica se a idade lida é igual a 999
    if idade == 999:
        break
    
    somatorio_idade += idade
    total_alunos += 1
    
# Cálculo da média
media = somatorio_idade / total_alunos

# Exibo as informações
print(f'Há {total_alunos} alunos na turma')
# Formato a média com 1 casa decimal
print(f'A média de idade do grupo é de {media:.1f}')
