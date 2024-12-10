#introução  condições if > elif > else 
"""
entrada = input("VOCÊ QUER ENTRAR NO SISTEMA?")
if entrada == "entrar" :
    print ("VOCÊ ENTROU DO SISTEMA")
    
elif entrada == "sair":
    print ("VOCÊ SAIU DO SISTEMA")
else:
    print("voce não digitou nada")

print(r"Ola \"men")"""

# Numeros inteiros
"""print(12)
soma = 2 + 3
int_ = int('1') #Transforma str em int 
idade = 30
maior_idade = (idade < 18) 
print(int_,type(int_)) #Type vai mostrar de qual clss do elemento entre (1) = inteiro
print(maior_idade) # False"""

# Teste 
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
print(nome)
condicao = False
print(idade)
if (float(altura) < 15):
        print(float(altura))
else: 
    altura_ = float(altura)
    print("Menor de idade. ",altura_)"""
    
#Atividade 1 
"""
valor_1 = input("Digite o 1 valor:")
valor_2 = input("Digite o 2 valor:")
if(valor_1 < valor_2):
    print(f'{valor_2 =} é maior que o ' f'{valor_1 =}')
else:
    print(f'{valor_1 =} é maior que o ' f'{valor_2 =}')
"""

#Atividade 2
"""
nome = input("Dgite o seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura\nEx 1.56: "))
imc = peso / (altura * altura)

print(nome," tem o imc de ",imc," e tem a altura de ",altura, " e pesa ",peso,"kg.")
# Em f-strings
pessoa_1 = f'{nome} tem o imc de {imc:.2f} e tem a altura de {altura:.2f}e pesa {peso} kg.'
print(pessoa_1)
"""

# funcão format
"""
a = 'a'
b = 'B'
c = 1.1
string = 'a={0} b={nome2} c={nome3:.2f}'
formato = string.format(a, nome2=b, nome3=c)
print(formato)
print(a)
"""
#Introduçãoao try/except
""" 
EXEMPLO DE ERROS
print(1234)
print(456)
int("a") <--


numero_str = input("Digite o numero para ser dobrado: ")

print(numero_str.isdigit())
numero_ = int(numero_str)
numero_float = float(numero_)
if numero_str.isdigit():{
    print(f"Este é o dobro de {numero_float*2}")
}
else: {
    print("Isto não é um numero")
}
"""
#Codigo limpo
""" velocidade_c = 90 #velocidade atual do carro
br_carro = 340 # Br em qual o carro está


br_radar1 = 360 # local onde o está o 1 radar
radar1 = 90 # velocidade maxima permetida pelo radar
grau_radar = 1 # a distancia onde o radar pegar
passou_no_radar = velocidade_c >= radar1
local_onde_passou = br_carro <= (br_radar1 - 1) or br_carro <= (br_radar1 + 1)

if (local_onde_passou):{
    print("Carro passou pelo radar 1")
}
if (local_onde_passou and passou_no_radar):{
    print("Você será multado: ")
}
"""

# flag (Banderia) -- Marcar um local 
# None =  noa valor
# is e is not = é ou nao é (tipo, valor,identidade)
# id = identidade
""" 
condicao = True
passou_no_if = None
if condicao:
    print('Faça algo')
    passou_no_if = True 
else:
    print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('PASSOU NO IF')
    passou_no_if = True 
else:
    print('NÃO PASSOU NO IF')
"""
''' 
# id = identidade
v1 = 'a'
print (id(v1))
v2 = 'a'
print (id(v2))
'''
'''
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)
'''