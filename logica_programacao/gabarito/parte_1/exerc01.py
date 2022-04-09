'''
Faça um programa em python que leia 4 notas, calule e imprima a média aritmética do aluno.
'''

# Inicializo com 0 uma variável que receberá/somará todas as notas
somatorio_notas = 0 

# Utilizo a estrutura de repetição for pois já sei 
# quantas vezes preciso repetir um ação

# Uso a função range para gerar um iterável de tamanho 4
# Nesse caso usei o start como 1 (inlcusivo) e o end como 5
# (exclusivo)
for grau in range(1, 5):
    # Casting para float pois o input retorn string
    nota = float(input(f'Nota {grau}: '))
    # É a mesma coisa que somatorio_notas = somatorio_notas + nota
    somatorio_notas += nota

# Faço o cálculo da média
media = somatorio_notas / 4

# Imprimo na tela a média do aluno formatada com 2 casas decimais
print(f'A média do aluno foi {media:.2f}')
