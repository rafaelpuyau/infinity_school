'''
Faça um procedimento que recebe 3 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente.
'''

'''
Implementação para quando vermos Listas
def ordena_3(lista_crescente):
    lista_crescente.sort()
    return lista_crescente

lista = []
for num in range(1, 4):
    lista.append(int(input(f'Digite o {num}º número: ')))

print(f'Os números em ordem crescente: {ordena_3(lista)}')
'''

def ordena(a, b, c):
    '''
        Esta função recebe três números e retorna-os em ordem crescente
        
        params: 
            a -> int : inteiro e positivo
            b -> int : inteiro e positivo
            c -> int : inteiro e positivo
            
        return:
            retorna uma tupla com os números em ordem crescente
    '''
    if a < b and a < c and b < c:
        return a, b, c
    elif a < b and a < c and c < b:
        return a, c, b
    elif b < a and b < c and a < c:
        return b, a, c
    elif b < a and b < c and c < a:
        return b, c, a
    elif c < a and c < b and a < b:
        return c, a, b
    elif c < a and c < b and b < a:
        return c, b, a

    return tuple

num1 = int(input('1º número: '))
num2 = int(input('2º número: '))
num3 = int(input('3º número: '))

x, y, z = ordena(num1, num2, num3)

print(f'Os números em ordem crescente: {x}, {y}, {z}')
