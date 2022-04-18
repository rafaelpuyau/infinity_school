'''
Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor
'''

def retorna_somatorio(n):
    '''
        Esta função retorna o somatório de um valor informado pelo usuário
        
        params:
            n -> int : inteiro e positivo
        
        return:
            somatorio -> int : retorna o somatorio do valor informado
    '''
    somatorio = 0
    for i in range(1, n + 1):
        somatorio += i
        
    return somatorio

num = int(input('Número: '))
print(retorna_somatorio(num))
