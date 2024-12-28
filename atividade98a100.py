i = 0
print("Bom dia!!")
while i == 0:
    # CALCULO DO 1º DIGITO
    cpf_enviado_pelo_usuario = input("Digite o seu CPF abaixo \nSEM OS '.' E '-' |> ")
    digitos = 0
    
    # capturo os a quantidade de digitos e os numeros que foram digitados invalidos caso aja um cacter exibo a tela.
    for confirmar in cpf_enviado_pelo_usuario:
        try:
            digitos += 1
        except ValueError:
            print("Por favor, utilize somente numeros")
            break

    # Verico se á 11 digitos 
    print(f"{digitos=}")        
    if digitos < 11 or digitos > 11:
        print("Digite novamente os 11 digitos")
        continue
    else:
        print("Digitos validos")
        
    # Adicionando os numero convertido para int dentro de uma list
    cpf_gerado_pelo_calculo = []
    for numero_1 in cpf_enviado_pelo_usuario:
        numero_int = int(numero_1)
        cpf_gerado_pelo_calculo.append(numero_int)
    
    # Multiplicando  o valor de cada digito na lista por ordem
    digitos_multiplicados_1 = []
    maximo_1 = 0
    multiplicador_1 = 10
    for numero_1 in cpf_gerado_pelo_calculo:
        maximo_1 += 1
        if maximo_1 < 10:
            valor_1 = numero_1*multiplicador_1
            digitos_multiplicados_1.append(valor_1)
            multiplicador_1 -= 1
        else:
            break
    print(*digitos_multiplicados_1)
    
    # Soma de todos os digitos multiplicados
    soma_dos_digitos_1 = 0
    for numero_1 in digitos_multiplicados_1:
        soma_dos_digitos_1 += numero_1
    print(soma_dos_digitos_1)
    
    # Multiplicar a soma dos digitos por 10
    soma_multiplicado_por_dez_1 = soma_dos_digitos_1 * 10
    print(soma_multiplicado_por_dez_1)
    
    # Resto da divisão com 11 da soma dos digitos multiplicado por 10
    resto_da_divisão_1 = soma_multiplicado_por_dez_1 % 11
    print(resto_da_divisão_1)
    
    # O subustindo o penutimo digito
    if resto_da_divisão_1 <= 9:
        cpf_gerado_pelo_calculo.pop(9); cpf_gerado_pelo_calculo.insert(9,resto_da_divisão_1)
        print(f"O resto é |> {resto_da_divisão_1}")
        print(*cpf_gerado_pelo_calculo)
    else:
        cpf_gerado_pelo_calculo.pop(9); cpf_gerado_pelo_calculo.insert(9,0)
        print(f"O resto é |> 0")
        print(*cpf_gerado_pelo_calculo)
    
    # CALCULO DO 2º DIGITO
    # Multiplicando  o valor de cada digito na lista por ordem
    digitos_multiplicados_2 = []
    maximo_2 = 0
    multiplicador_2 = 11
    for numero_2 in cpf_gerado_pelo_calculo:
        maximo_2 += 1
        if maximo_2 < 11:
            valor_2 = numero_2*multiplicador_2
            digitos_multiplicados_2.append(valor_2)
            multiplicador_2 -= 1
        else:
            break
    print(*digitos_multiplicados_2)
    
    # Soma de todos os digitos multiplicados
    soma_dos_digitos_2 = 0
    for numero_2 in digitos_multiplicados_2:
        soma_dos_digitos_2 += numero_2
    print(soma_dos_digitos_2)
    
    # Multiplicar a soma dos digitos por 10
    soma_multiplicado_por_dez_2 = soma_dos_digitos_2 * 10
    print(soma_multiplicado_por_dez_2)
    
    # Resto da divisão com 22 da soma dos digitos multiplicado por 10
    resto_da_divisão_2 = soma_multiplicado_por_dez_2 % 11
    print(resto_da_divisão_2)
    
    # O subustindo o penutimo digito
    if resto_da_divisão_2 <= 9:
        cpf_gerado_pelo_calculo.pop(10); cpf_gerado_pelo_calculo.insert(10,resto_da_divisão_2)
        print(f"O resto é |> {resto_da_divisão_2}")
        print(*cpf_gerado_pelo_calculo)
    else:
        cpf_gerado_pelo_calculo.pop(9); cpf_gerado_pelo_calculo.insert(10,0)
        print(f"O resto é |> 0")
        print(*cpf_gerado_pelo_calculo)
        
        
    CPF_enviado_pelo_usuario = []
    for numero in cpf_enviado_pelo_usuario:
        CPF_enviado_pelo_usuario.append(int(numero)) 
        
    condicao = CPF_enviado_pelo_usuario == cpf_gerado_pelo_calculo
    if condicao:
        print("CPF VALIDO")
    else:
        print("CPF Invalido")
    break