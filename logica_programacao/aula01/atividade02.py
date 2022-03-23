'''
Transformar uma temperatura de Fahrenheit para Celcius

Fórmula : celcius = (fahrenheit - 32) * 5 / 9
'''

# Solcito que o usuário entre com a temperatura em fahrenheit
fahrenheit = float(input('Digite a temperatura [ºF]: '))

# Aplico a fórmula depois de receber a temperatura em Fahrenheit e 
# transformar através do casting em float
celcius = (fahrenheit - 32 ) * 5 / 9

# Imprimo na tela a temperatura em convertida para Celcius
# Formato a saída do grau Celcius para 2 casas decimais

# Com f-string
print(f'{fahrenheit}ºF equivale à {celcius:.2f}ºC')

# Com o método format()
print('{0}ºF equivale à {1:.2f}ºC'.format(fahrenheit, celcius))