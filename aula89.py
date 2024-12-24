""" 
Exercicio
Exiba os indices da lista
0 Maria
1 João
2 Pedro
"""
Lista_de_nomes = ['Pedro','João','Lucas','Ramos','Costa']
Lista_de_nomes.append('Maria')


# for nomes in Lista_de_nomes:
#    print(nomes)

for indice, nome in enumerate(Lista_de_nomes):
    print(indice, nome)