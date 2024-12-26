i = 0
while i == 0:
    print("Bom dia!! \nDigite o seu CPF abaixo")
    CPF_cru = input("SEM OS '.' E '-' |> ")
    digitos = 0
    
    # capturo os a quantidade de digitos e os numeros que foram digitados invalidos caso aja um cacter exibo a tela.
    for confirmar in CPF_cru:
        try:
            digitos += 1
        except ValueError:
            print("Por favor, utilize somente numeros")
            break

    # Verico se á 11 digitos 
    print(f"{digitos=}")        
    if digitos < 11: 
        print("Digite novamente os 11 digitos")
        continue
    else:
        print("Digitos validos")
        
    # Adicionando os numero convertido para int dentro de uma list
    cpf = []
    for numero in CPF_cru:
        numero_int = int(numero)
        cpf.append(numero_int)
        
    break