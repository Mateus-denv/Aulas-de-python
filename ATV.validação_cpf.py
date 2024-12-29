# Etapas 
"""
1. CALCULO DO 1º DIGITO - Criar um While True
    1.1 Receber os dados do User convertenduos em int.
    1.2 Tratar os dados recibidos: 
        1.2.a Verificar se foram digitatos somente numeros, caso contrario o programa se repete.
        1.2.b Verificar quantidade de digitos é valida, caso contrario o programa se repete.
    1.3 Multiplicar cada valor por um contagem regrasiva começando do 10.
    1.4 Coleta a soma dos resultados dos 9 primeiros digitos e soma-los.
    1.5 Multiplicar a soma desses valores por 10.
    1.6 Obter o resto da multipicação por % 11.
    1.7 Foram ciaridas 2 lista, a 1º para armazena o valor que o usuario enviou, e a 2º para armazena o valor que o programa gerou.
    1.8 Se o resto for maior que 9 o penúltimo numero devera se torma 0, caso contrario permance o valor do resto.
2. CALCULO DO 2º DIGITO
    Obs.: Nesse caso ja posssuimos o 10º digito então incluiremos ele a conta
    2.1 Multiplicar cada valor por um contagem regrasiva começando do 11.
    2.2 Coleta a soma dos resultados dos 10 primeiros digitos e soma-los.
    2.3 Multiplicar a soma desses valores por 10.
    2.4 Obter o resto da multipicação por % 11.
    2.5 Se o resto for maior que 9 o penúltimo numero devera se torma 0, caso contrario permance o valor do resto.
"""
# ETAPA 1.
while True:
    # 1.1
    try:
        CPF_ENVIADO_POR_USER = int(input("Digite o seu CPF abaixo \nSOMENTE NUMEROS\n|>"))
    # 1.2
    except ValueError:
        # 1.2.a
        print("Digite somente numeros!!!")
        continue
    # 1.2.b
    cont = 0
    for digitos in str(CPF_ENVIADO_POR_USER):
        cont += 1
    condicao = "Quantidade de digitos validos" if cont == 11 else "Quantidade de digitos invalido"
    print(condicao)
    if cont != 11:
        continue
    
    # 1.3
    soma_dos_nove_primerio_digitos = 0
    nove_primeiros_digitos = str(CPF_ENVIADO_POR_USER)[:9]
    multiplicador = 10
    for digitos in nove_primeiros_digitos:
        # 1.4
        soma_dos_nove_primerio_digitos += int(digitos) * multiplicador
        multiplicador -= 1
    # 1.5
    numeros_multip_por_10 = soma_dos_nove_primerio_digitos * 10
    # 1.6
    resto_multip_por_10_1 = numeros_multip_por_10 % 11
    
    # 1.7
    cpf_gerado_por_programa = []
    cpf_enviador_por_user = []
    for digito in str(CPF_ENVIADO_POR_USER):
        cpf_gerado_por_programa.append(digito)
        cpf_enviador_por_user.append(digito)
    # 1.8
    if resto_multip_por_10_1 > 9:
        print(f"\nEste digito [{resto_multip_por_10_1}] não é valido e será substituido para '0'.")
        cpf_gerado_por_programa.pop(9)
        cpf_gerado_por_programa.insert(9, "0")
    else:
        print(f"\nEste digito [{resto_multip_por_10_1}] é valido.")
        cpf_gerado_por_programa.pop(9)
        cpf_gerado_por_programa.insert(9, str(resto_multip_por_10_1))
    print("\nEnviado por você: ",*cpf_enviador_por_user, sep="")
    print("Gerado pelo programa: ",*cpf_gerado_por_programa,sep= "")
    
    # 2.1 
    soma_dos_dez_primeiro_digitos = 0
    dez_primeiros_digitos = cpf_gerado_por_programa[:10]
    multiplicador = 11
    # 2.2
    for digito in dez_primeiros_digitos:
        soma_dos_dez_primeiro_digitos += int(digito) * multiplicador
        multiplicador -=1
    # 2.3
    numeros_multip_por_11 = soma_dos_dez_primeiro_digitos * 10
    # 2.4
    resto_multip_por_10_2 = numeros_multip_por_11 % 11
    # 2.5
    if resto_multip_por_10_2 > 9:
        print(f"\nEste digito [{resto_multip_por_10_2}] não é valido e será substituido para '0'.")
        cpf_gerado_por_programa.pop(10)
        cpf_gerado_por_programa.insert(10, "0")
    else:
        print(f"\nEste digito [{resto_multip_por_10_2}] é valido.")
        cpf_gerado_por_programa.pop(10)
        cpf_gerado_por_programa.insert(10, str(resto_multip_por_10_2))
    print("\nEnviado por você: ",*cpf_enviador_por_user, sep="")
    print("Gerado pelo programa: ",*cpf_gerado_por_programa,sep= "")
    
    
    for i, digito in enumerate(cpf_gerado_por_programa):
        if cpf_enviador_por_user[i] == cpf_gerado_por_programa[i]:
            if i == 11:  
                print("Seu CPF É VALIDO")
        
    break