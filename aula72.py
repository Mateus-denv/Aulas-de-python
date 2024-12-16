# Laço de repetição FOR
texto = "oi"
"""
i = 0
tamanho_texto = len(texto)
# WHILE é utilizado qundo nos *não* sabemos quantos laços de repetiçoes seram utilados

    while i < tamanho_texto:
    print(texto[i],i)
    i += 1
"""
# FOR é utilizado qundo nos sabemos quantos laços de repetiçoes seram utilados
novo_texto = ''
for letra in texto:
    novo_texto += f'-{letra}'
    print(letra)
print(novo_texto)