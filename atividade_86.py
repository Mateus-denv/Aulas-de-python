""" 
Exercicio
Exiba os indices da lista
0 Maria
1 João
2 Pedro
"""
Nomes = ["Maria", "João", "Pedro"]
#Criei um varevel so pra acumular a quantidade de valores na lista
indices = range(len(Nomes)) # Quando so usando 1 sintaxe range é "O número onde a sequência para (não é incluído na sequência)."

for indices in len(Nomes):
    print(indices, Nomes[indices])