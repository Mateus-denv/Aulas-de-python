# Calculadora com while
"""
numero = input("Digite um numero:")
if numero == '':
    print(f"Numero invalido")
else:
    numero_int = int(numero)
    print("Digite o que deseija \n1-SOMAR\n2-SUBITRARIR\n3-MULTIPLICAR\n4-DIVIDIR")
    opcao_int = int(input("|>"))
    if opcao_int == 1:
        contador = 1
        while  contador <= 10:
            print(f"{numero_int} + {contador} = {numero_int+contador}")
            contador += 1
    elif opcao_int == 2:
        contador = 1
        while  contador <= 10:
            print(f"{numero_int} - {contador} = {numero_int-contador}")
            contador += 1
    elif opcao_int == 3:
        contador = 1
        while  contador <= 10:
            print(f"{numero_int} x {contador} = {numero_int*contador}")
            contador += 1
    elif opcao_int == 4:
        contador = 1
        numero_float = float(numero_int)
        while  contador <= 10:
            print(f"{numero_float:.0f} / {contador} = {numero_float/contador:.2f}")
            contador += 1
    else:
        print("Opção invalida")

"""
"""
while True:
    numero_1 = int(input("Digite um numero: "))
    numero_2 = int(input("Digite segundo numero numero:"))
    opcao = int(input("Qual o operador logico você quer utlizar?\n1-SOMAR\n2-SUBITRARIR\n3-MULTIPLICAR\n4-DIVIDIR\n5-PARA/SAIR: "))
    
    # lower -> trasforma em minusculo
    # Startswinth -> começa com s? True or False
    if opcao == 1:
        print(f"A SOMA DE {numero_1} + {numero_2} é igual a {numero_1+numero_2}")
        sair = input("Quer sair: \n[S]SIM\n|>").lower().startswith('s')
    elif opcao == 2:
        print(f"A SUBTRAÇAO DE {numero_1} - {numero_2} é igual a {numero_1-numero_2}")
        sair = input("Quer sair: \n[S]SIM\n|>").lower().startswith('s')
    elif opcao == 3:
        print(f"A MULTIPLICAÇÃO DE {numero_1} * {numero_2} é igual a {numero_1*numero_2}")
        sair = input("Quer sair: \n[S]SIM\n|>").lower().startswith('s')
    elif opcao == 4:
        numero_1_f = float(numero_1); numero_2_f = float(numero_2)
        print(f"A DIVISÃO DE {numero_1_f:.1f} / {numero_2_f:.1f} é igual a {numero_1_f/numero_2_f:.2f}")
        sair = input("Quer sair: \n[S]SIM\n|>").lower().startswith('s')
    elif sair is True:
        print("Saindo...")
        break
    else:
        print("Opção invalida")
print("ACABOU/SAIU")
"""
while True:
    numero_1 = float(input("Digite um numero: "))
    numero_2 = float(input("Digite segundo numero numero: "))
    operadores = input("Qual o operador logico você quer utlizar?\n1-SOMAR\n2-SUBITRARIR\n3-MULTIPLICAR\n4-DIVIDIR\n")
    numeros_validos = None
    try:
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None: # is = é?
        print("Os numeros digitados estão invalidos")
        continue
    # not in -> não esta entre
    operacoes_permitidas = "1234"
    if operadores not in operacoes_permitidas: # Verifica se oque o usuario digito esta entre oque é permitido.
        print("Operação invalida")
        continue
    if len(operadores) > 1:
        print("Digite apenas 1 operador")
        continue
    if operadores == '1':
        print(f"{numero_1} + {numero_2} = {numero_1 + numero_2} ")
    elif operadores == '2':
        print(f"{numero_1} - {numero_2} = {numero_1 - numero_2} ")
    elif operadores == '3':
        print(f"{numero_1} * {numero_2} = {numero_1 * numero_2} ")
    elif operadores == '4':
        print(f"{numero_1} / {numero_2} = {numero_1 / numero_2} ")
    else:
        print("Não deveria entrar aqui?")
    # .lower() -> trasforma em minusculo
    # .startswinth() -> começa com s? True or False
    sair = input("Deseija sair? \n[s] Sair\n|>").lower().startswith("s")
    if sair is True:
        break