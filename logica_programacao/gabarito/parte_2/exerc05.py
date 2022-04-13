'''
Faça um programa que leia duas notas de um aluno em uma determinada matéria e mostre na tela sua média na disciplina em questão. (Ex. A média entre 7.3 e 8.7 é de 8)
'''

# Lendo as notas do aluno e fazendo o casting para float
nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))

# Cálculo da média
media = (nota_1 + nota_2) / 2

# Formatação da média com 2 casas decimais
print(f'A média entre {nota_1} e {nota_2} é de {media:.2f}')
