""" 
FAÇA UM LISTA DE COMPRAS COM LISTAS[] O USUARIO DEVE TER A POSSIVILIDADE INSERIR, APAGAR E LISTA VALORES DA SUA LISTA

# NÃO PERMITA QUE O PROGRAMA QUEBRE COM ERROS DE INDICIESI INEXISTENTES
"""
frutas = []
Valores = []

i = 0
print('Olá, bem vindo ao Hortifrut')
while True:
    nome = input("Digite o seu nome:")
    if len(nome) < 2:
        print("Nome inlegivel")
        continue
    
    while i == 0:
        adc_frut = input("\nDiga qual fruta deseija incerir: ")
        frutas.insert(i, adc_frut)
        
        adc_valor_frut = int(input("Diga qual Valor dessa fruta deseija incerir: "))
        Valores.insert(i, adc_valor_frut)
        mais = int(input("Adicionar mais?\n1-SIM\n2-NÃO\n"))
        if mais >= 2:
            print("Até mais!!!")
            break
        continue
    
    apagar = int(input("\nDeseja retira alguma fruta \n1-S\n2-N\n") )
    if apagar <= 1:
        i = 0
        apagar_fruta = input("\nDigite a fruta: ")
        for fruta in frutas:
            print(fruta)
            if  fruta == apagar_fruta:
                frutas.pop(i)
                Valores.pop(i)
            i += 1
        if i == len(frutas):
            print("Essa fruta não existe")
            
    i = 0
    indice = range(len(frutas))
    print("\nFrutas diponiveis:")
    for i in indice:
        print("\nFruta",frutas[i],"\nValor R$",Valores[i])
        