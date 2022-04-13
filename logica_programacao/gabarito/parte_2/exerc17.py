'''
Faça um programa que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média deste aluno e veja se teve ou não um bom aproveitamento. Se maior ou igual a 7, aprovado. Se menor que 5 reprovado, senão se maior ou igual a 5 e menor que 7, em recuperação.
'''

# Pego o nome do aluno
nome_aluno = input('Nome do aluno: ')

# Inicializo a variável que somará as notas do aluno
somatorio_notas = 0

# Uso o laço for pois sei que preciso ler 2 vezes as notas do aluno
# A função Range gera um iterável de tamanho 2
for av in range(1, 3):
    nota = float(input(f'{av}ª nota: '))
    somatorio_notas += nota
    
# Cálculo da média
media = somatorio_notas / 2

# Exibo na tela a média do aluno formatada com 2 casas decimais
print(f'Média do aluno: {media:.2f}')

# Bloco condicional para verificar a média e informar o aproveitamento do aluno
if media >= 7:
    print(f'{nome_aluno} está APROVADO')
elif media >= 5:
    print(f'{nome_aluno} está EM RECUPERAÇÃO')
else:
    print(f'{nome_aluno} está REPROVADO')
