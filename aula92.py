""" 
Imprecisão de numeros de ponto flutuante
E soluções
"""


"""
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(f"{numero_3}")
"""
# Solução
import decimal
numero_1 = decimal.Decimal("0.1")
numero_2 = decimal.Decimal("0.7")
numero_3 = numero_1 + numero_2
print(f"{numero_3}")
print(f"{numero_3:.2f}")
print(round(numero_3, 2))