"""
Introdução a Tuplas
"""
# So usar sem [] - são imutaveis 
Nomes = ['Maria','Helena','Luiz']
nome1, nome2, nome3 ='Maria','Helena','Luiz'
print(nome2)
nome1, *resto = ['Maria','Helena','Luiz']
print(resto)

# Convertando em Tuplas
Nomes = tuple(Nomes)
# Convertando em Lista
Nomes = list(Nomes)

Nomes[1] = "Conseguir"
print(Nomes)