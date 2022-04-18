'''
Elaborar um algoritmo que calcule a área de triângulos , quantos o usuário quiser calcular separe a função com o nome “calcula_triangulo”. 

area = b * h / 2

'''

def calcula_triangulo(base, altura):
    '''
        Essa função calcula a área de um triângulo
        
        params:
            base -> float : base do triângulo
            altura -> float : altura do triângulo
            
        return:
            retorna a área do triângulo -> float
            Fórmula base * altura / 2
    '''
    return base * altura / 2


while True:
    base = float(input('Base do Triângulo: '))
    altura = float(input('Altura do Triângulo: '))
    
    area = calcula_triangulo(base, altura)
    print(f'A área do triângulo é {area:.2f}')
    
    continuar = input('Deseja calcular a área de outro triângulo? [S/N] ').upper()[0]
    
    if continuar == 'N':
        break
