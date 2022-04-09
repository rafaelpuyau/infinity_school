'''
Faça um programa que leia o saldo da conta corrente do usuário e faça o reajuste de 1%. Imprimir na tela o saldo reajustado.
'''

# Leitura dos dados solicitados
# Casting para float pois o saldo possui casa decimal
saldo_cc = float(input('Saldo da Conta-Corrente [R$]: '))

# Cálculo do reajuste de 1%
saldo_reajustado = saldo_cc * 1.01

# ATENÇÃO:
# Ou forma de fazer o reajuste
# reajuste = saldo_cc * 0.01
# saldo_reajustado = saldo_cc + reajuste

# Formato a saída do saldo reajustado para 2 casas decimais
print(f'Saldo reajustado R${saldo_reajustado:.2f}')
