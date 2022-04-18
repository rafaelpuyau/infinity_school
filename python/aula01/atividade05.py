'''
Faça uma função que receba um valor inteiro e positivo e calcula o seu fatorial.
'''

def fatorial(n):
    '''
        Esta função calcula o fatorial de um número inteiro e positivo
        
        params: 
            n -> int : inteiro e positivo
        
        return
            retorna o fatorial do número
    '''
    if n == 0 or n == 1:
        return 1
    
    for i in range(1, n):
        n *= i
        
    return n

num = int(input('Número: '))
print(f'{num}! = {fatorial(num)}')
