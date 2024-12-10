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
while True:
    numero_1 = int(input("Digite um numero: "))
    numero_2 = int(input("Digite segundo numero numero:"))
    opcao = int(input("Qual o operador logico você quer utlizar?\n1-SOMAR\n2-SUBITRARIR\n3-MULTIPLICAR\n4-DIVIDIR\n5-PARA/SAIR: "))
    
    # lower -> trasforma em minusculo
    # Startswinth -> começa com s? True or False
    if opcao == 1:
        print(f"A SOMA DE {numero_1} + {numero_2} é igual a {numero_1+numero_2}")
        sair = input("Quer sair: [S]SIM").lower().startswith('s')
    elif opcao == 2:
        print(f"A SUBTRAÇAO DE {numero_1} - {numero_2} é igual a {numero_1-numero_2}")
        sair = input("Quer sair: [S]SIM").lower().startswith('s')
    elif opcao == 3:
        print(f"A MULTIPLICAÇÃO DE {numero_1} * {numero_2} é igual a {numero_1*numero_2}")
        sair = input("Quer sair: [S]SIM").lower().startswith('s')
    elif opcao == 4:
        numero_1_f = float(numero_1); numero_2_f = float(numero_2)
        print(f"A DIVISÃO DE {numero_1_f:.1f} / {numero_2_f:.1f} é igual a {numero_1_f/numero_2_f:.2f}")
        sair = input("Quer sair: [S]SIM").lower().startswith('s')
    elif sair is True:
        print("Saindo...")
        break
    else:
        print("Opção invalida")
print("ACABOU/SAIU")