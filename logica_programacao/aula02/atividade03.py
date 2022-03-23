'''
Receber do usuário a quantidade de respiradores e a porcentagem de ocupação de 5 hospitais em Salvador, caso algum desses hospitais tenham menos que 50 respiradores e a taxa ocupacional esteja maior que 60%, serão adicionados mais 5.
'''

# Dados informados pelo usuário para os 5 hospitais

# Hospital 1
print('Hospital 1')
respiradores1 = int(input('Quantidade de respiradores: '))
ocupacao1 = int(input('Porcentagem de ocupação: ')) 

# Valido as informações para saber se adiciona mais 5 respiradores ou não 
if respiradores1 < 50 and ocupacao1 > 60:
    respiradores1 += 5
    print(f'Aumentamos a quantidadede respiradores para {respiradores1}')
    
# REPETIR ESSA LÓGICA PARA OS HOSPITAIS RESTANTES
# Nesse momento não usaremos laços de repetição ainda...

# Hospital 2
print('Hospital 2')
respiradores2 = int(input('Quantidade de respiradores: '))
ocupacao2 = int(input('Porcentagem de ocupação: ')) 

# Valido as informações para saber se adiciona mais 5 respiradores ou não 
if respiradores2 < 50 and ocupacao2 > 60:
    respiradores2 += 5
    print(f'Aumentamos a quantidadede respiradores para {respiradores2}')
    
# Hospital 3
print('Hospital 3')
respiradores3 = int(input('Quantidade de respiradores: '))
ocupacao3 = int(input('Porcentagem de ocupação: ')) 

# Valido as informações para saber se adiciona mais 5 respiradores ou não 
if respiradores3 < 50 and ocupacao3 > 60:
    respiradores3 += 5
    print(f'Aumentamos a quantidadede respiradores para {respiradores3}')
    
# Hospital 4
print('Hospital 4')
respiradores4 = int(input('Quantidade de respiradores: '))
ocupacao4 = int(input('Porcentagem de ocupação: ')) 

# Valido as informações para saber se adiciona mais 5 respiradores ou não 
if respiradores4 < 50 and ocupacao4 > 60:
    respiradores4 += 5
    print(f'Aumentamos a quantidadede respiradores para {respiradores4}')

# Hospital 5
print('Hospital 5')
respiradores5 = int(input('Quantidade de respiradores: '))
ocupacao5 = int(input('Porcentagem de ocupação: ')) 

# Valido as informações para saber se adiciona mais 5 respiradores ou não 
if respiradores5 < 50 and ocupacao5 > 60:
    respiradores5 += 5
    print(f'Aumentamos a quantidadede respiradores para {respiradores5}')
    
