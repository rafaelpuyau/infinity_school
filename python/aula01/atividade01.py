'''
Crie um algoritmo em Python, que dado dois números informados pelo usuário e sua operação (das 4 operações básicas da matemática), realize os cálculos adequados dentro de funções.
'''

def realizar_calculo(op1, op2, op):
    '''
        Está função realiza as 4 operações básicas da matemática
        
        param:
            op1 -> int : 1º operando
            op2 -> int : 2º operando
            op -> str : recebe uma das 4 operações básicas (+, -, *, /)
            
        return:
            Retorna o resultado da operação passada
    '''
    if op == '+':
        return True, op1 + op2
    elif op == '-':
        return True, op1 - op2
    elif op == '*':
        return True, op1 * op2
    elif op == '/' and op2 != 0:
        return True, op1 / op2
    else:
        return False, 'Operação inválida'
    

num1 = int(input('Digite um número inteiro e positivo: '))
num2 = int(input('Digite um outro número inteiro e positivo: '))
operacao = input('Qual operação deseja realizar com os números informados [ +, -, *, / ]: ')

result = realizar_calculo(num1, num2, operacao)

if result[0]:
    print(f'{num1} {operacao} {num2} = {result[1]}')
else:
    print(result[1])
