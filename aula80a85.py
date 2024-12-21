""" 
for in com lista
"""
Nomes = ["Maria", "Helena", "Luis"]
Nomes.append("Pedro")

indices = range(len(Nomes)) # Ver quantas coisas tem na lista "VETOR"

for contador in indices:
    print(f"{contador} {Nomes[contador]}")
