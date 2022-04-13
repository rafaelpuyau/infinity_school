'''
Faça um programa que pergunte ao usuário um número inteiro e positivo qualquer e mostre uma contagem até esse valor. Se o usuário digital 15, por exemplo, a saída deverá ser: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 Acabou!
'''

# Leio um número digita do pelo usuário e faço o casting para inteiro
numero = int(input('Digite um número inteiro e positivo: '))

# Para incluir o número informado pelo usuário no iterável, preciso somar 1 a ele
for n in range(1, numero + 1):
    print(n, end=' ')
    
print('Acabou!')
