'''
Escreva uma função que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
'''

def conta_vogal(texto):
    '''
        Esta função conta o número de ocorrências de vogais em um texto
        
        params:
            texto -> str : texto a ser analisado
        
        return:
            retorna um dicionário com o número de ocorrências de cada vogal num determinado texto -> dict
    '''
    vogal_dict = {}
    for vogal in texto.lower():
        if vogal in 'aeiou':
            vogal_dict[vogal] = texto.lower().count(vogal)
    return vogal_dict
        

txt = input('Digite um texto: ')
print(conta_vogal(txt))


