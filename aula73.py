""" 
For + range
range -> range (start, stop, step)

numeros = range(0, 100, 8)
for numero in numeros:
    print(numero)

Interavel -> é elemento que pode te entregar uma coisa por vez Ex.: str, range, etc (__iter__) -> "_" é dander
Interador -> é quem sabe entregar um valor por vez
next -> me entregue o proximo valor 
iter -> me entrega seu iterador
"""
texto = "LUIS"
iteratador = iter(texto)
# print(texto.__next__()) # ou print(next(texto))

# Como o for fuciona por debaixo dos panos 
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

