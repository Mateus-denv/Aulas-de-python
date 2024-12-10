contador = 0
numero = input("Digite um numero inteiro :")

while contador <= 100:
    contador += 1
    
    if contador % 2 == 0:
        print("Numero foi encontrado par")
        continue
    print(contador)
    if contador % 2 != 0:
        print("Numero impar")
    if contador == 40:
        break
        
