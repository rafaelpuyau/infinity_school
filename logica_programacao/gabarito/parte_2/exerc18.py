'''
Faça um programa que leia um determinado ano e mostre se este ano é Bissexto ou não. OBS: Procure a regra para saber se um ano é bissexto.
'''

# Regra para ano bissexto
# Para o ano ser bissexto, o ano deve ser:
# - Divisível por 4 : sendo assim, a divisão é exata com o resto igual a zero
# - Não pode ser divisível por 100 : com isso, a divisão não é exata, ou seja, deixa resto diferente de zero
# - Pode ser que seja divisível por 400 : caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero

# Leio o ano e faço o casting para inteiro
ano = int(input('Informe um ano para saber se é ou não Bissexto: '))

# Testo se o ano é bissexto pelas regras acima
if ano % 4 == 0 and ano % 100 != 0:
    print('Bissexto')
elif ano % 400 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')
