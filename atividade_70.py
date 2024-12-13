frase  = 'O Phyton é uma linguagem de programação multiparadigma. Phyton foi criado por Guido vam Rossum'.upper()
# .upper() -> Deixa todo o texto maiusculo
i = 0
letra_q_apreceu_mais = ""
qtd_q_mais_aparece = 0
while i < len(frase):
    """ 
    # Não permite a caputura de espaços " "
    
    if letra_atual == " ":
        i += 1
        continue
        
    """
    if frase[i] != " ": # Não permite a caputura de espaços " "
        letra_atual = frase[i] # Adiciona a letra diacordo o contador 
        
        quantas_veses_ela_aparece = frase.count(letra_atual) # .count() é utilizado para conta quantas vezes uma letra, palavra, numero ou frase etc... aparece em um texto/palavra em uma string.
        
        if qtd_q_mais_aparece < quantas_veses_ela_aparece:
            print(letra_atual)
            qtd_q_mais_aparece = quantas_veses_ela_aparece
            letra_q_apreceu_mais = letra_atual
        print(letra_atual," |> ",quantas_veses_ela_aparece)
    i += 1
else:
    print(f"A letra com a maior quantidade de vezes que apreceu foi a '{letra_q_apreceu_mais}' ela apareceu {qtd_q_mais_aparece}x.")