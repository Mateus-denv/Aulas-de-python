""" While/else"""
nome = "Mateus"
i = 0
while i < len(nome):
    letra = nome[i]
    if letra == ' ':
        break
    print(letra)
    i += 1
else: 
    print("O else foi executado")
print("Fora do while")