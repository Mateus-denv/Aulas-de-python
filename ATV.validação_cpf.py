# Etapas 
"""
1. CALCULO DO 1º DIGITO
    1.1 Receber os dados do User convertenduos em int
    1.2 Tratar os dados: 
        1.2.a Verificar se foram digitatos somente numeros  1.2.b Verificar quantidade de digitos é valida
    1.3 Multiplicar cada valor por um contagem regrasiva começando do 10
    1.4 Coleta a soma dos resultados dos 9 primeiros digitos e soma-los

"""
while True:
    # ETAPA 1.
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
    
    1.3
    soma_dos_nove_primerio_digitos = 0
    nove_primeiros_digitos = str(CPF_ENVIADO_POR_USER)[:9]
    multiplicador = 10
    for digitos in nove_primeiros_digitos:
        print(digitos)
        soma_dos_nove_primerio_digitos += int(digitos) * multiplicador
        multiplicador -= 1
        print(soma_dos_nove_primerio_digitos)

    break