# Desenpacotamento na chamada das funções
# De metodos e funções

string = 'ABCD'
lista = ['  OI',' DIEGO','      BRITO']
tupla = 'SEJA','BEM','VINDO'
print(*lista)

"""a, b ,c = lista
print(lista)"""

lista_ofc = []
for cont, palavra in enumerate(lista):
    lista_ofc.append(lista[cont].strip())
print(*lista_ofc)
print(*tupla)
print(*string, sep='')


"""for palavras in lista:
    print(palavras,end= '\n')"""