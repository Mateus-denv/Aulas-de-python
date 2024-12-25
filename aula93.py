""" 
# Split e join com list e str 

split - divide uma string
join - une uma string

"""
frase = 'Matheus              ,é lindo         '
lista_de_palavras_crua = frase.split(',')

lista_de_palavras = []
for i, frase in enumerate(lista_de_palavras_crua): # Strip tira o espaço do inicio e fim do caractr da lista
    lista_de_palavras.append(lista_de_palavras_crua[i].strip())
    
print(lista_de_palavras_crua)
print(lista_de_palavras)
nome = "    troxa  "
print(nome.strip())