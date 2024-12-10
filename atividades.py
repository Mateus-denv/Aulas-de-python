"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#RESPOSTA 1:
numero = input("Digite um numero: ") # Pede ao USUARIO um numero

if numero.isdigit(): # Verifca se você digitou um numero inteiro
    numero_float = float(numero) # Transforma em float
    par = numero_float % 2 == 0 # Confesere se é par ou não
    if par: # Se for par 
        print(f"O numero {numero} é par")
    else: # Se não for par é impar
        print(f"O numero {numero} é impar")
else:
    print("Voce não digitou um numero inteiro.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# RESPOSTA 2
hora = input("Digite a Hora atual: ")
try: 
    hora_atual = float(hora)    
    bomDia = hora_atual < 11.59
    boaTarde =  hora_atual >= 12.00 and hora_atual < 17.59
    boaNoite = hora_atual >= 18.00 and hora_atual < 23.59
    if bomDia:
        print("BOM DIA")
    
    elif boaTarde:
        print("BOA TARDE")  
    elif boaNoite:
        print("BOA NOITE")
    else:
        print("Numero não existe essa hora.")
    pass
except:
    print("Digite somente numeros.")

"""hora_atual = float(hora)
if bomDia:
    print("\nBOM DIA")

elif boaTarde:
    print("\nBOA TARDE")

else:
    print("\nBOA NOITE")"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("\nDigite o seu primeiro nome: ")
tamanho_nome = len(nome)
if tamanho_nome >= 2:
    if tamanho_nome >= 4:
        print("Seu nome é curto")
    elif tamanho_nome >= 5:
        print("Seu nome é nomral")
    else:
        print("Seu nome é grande")
else:
    print("Digite mais de 1 letra")
