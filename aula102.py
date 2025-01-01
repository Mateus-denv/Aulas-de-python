# Solução do para possiveis erros Validação de CPF

# Erro 1: O uso de outros caracteres pelo usuario
# Solução 1
"""cpf_enviador_por_user = input("Digite o seu CPF abaixo \nSOMENTE NUMEROS\n|>").replace("-","")"""
# Solução 2
import re
entrada = input("Digite o seu CPF abaixo \nSOMENTE NUMEROS\n|>")
cpf_enviador_por_user = re.sub(r'[^0-9]','',entrada)

print(cpf_enviador_por_user)
# Erro 2: O uso de caracter repetidos 
# Solução 1
caracter_repedito = entrada == entrada[0]*len(entrada)
if caracter_repedito:
    print("Refaça")