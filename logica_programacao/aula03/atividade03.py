'''
Você foi convidado a desenvolver um módulo de um sistema acadêmico. Você precisa capturar quantas notas o usuário necessitar e calcular a média dela, exibindo o resultado final
'''

# ATENÇÃO : pegaremos apenas 3 notas

# Inicialização da variável media com zero
media = 0 

# Laço FOR com a função range que gera um iterável com 3 elementos, indo de 1 à 3
for n in range(1, 4):
    #Solicitação da entrada de dados do usuário com o casting para float
    nota = float(input(f'Nota {n}: '))
    # Somo as notas e armazeno na variável média
    media += nota

# Faço a divisão por 3 segundo a nossa definição anterior
media /= 3

# Mostro na tela a média do aluno com formatação de 1 casa decimal
print(f'A média do aluno foi {media:.1f}')
