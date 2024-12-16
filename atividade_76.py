""" 
FAÇA UM JOGO PARA O USUARIO ADIVINHAR QUAL A PALAVRA SECRETA
VOCÊ VAI PROPOR UMA PALAVRA PASSE SECRETA QUALQUER E VAI DAR A POSSIBILIDADE PARA Q O USUARIO DIGITE APENAS UMA LETRA.

QUANDO O USUARIO DIGITAR A VOCE DEVE CONFERIR SE A LETRA DIGITADA ESTÁ NA PALAVRA SECRETA
 - pega letra que o usuario digitou e conferir passando por cada letra da palavra_s

SE A LETRA DIGITADA ESTIVER NA LETRA SECRETA EXIBA A LETRA
SE A LETRA DIGITADA NÃO ESTIVER EXIBA UM *
FAÇA UMA CONTAGUEM DE TENTATIVAS

"""
palavra_secreta = "Matheus"
print("Olá")
print("Tente adivinha a palavra secreta")
palavra = ''
for i in palavra_secreta:
    palavra += "*"
print("Digite uma letra: ")
tentativas = 3
while tentativas <= 3 and tentativas > 0:
    letra_user = input("")
    for j in palavra_secreta:
        if letra_user == j:
            palavra += f'{letra_user}'
        elif palavra != "*":
            print()
    print(f"{palavra}")
else:
    print("Você atingiu o maximo de tentantivas")
print("Até mais!!!")

len(palavra_secreta)