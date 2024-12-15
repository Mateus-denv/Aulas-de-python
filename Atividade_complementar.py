# Atividade feita com todos assuntos dados até o momento
print("::::::::::BEM VINDO A FILMAX::::::::::")
i = 0
while i == 0:
    nome = input("Digite o seu nome: ")
    if len(nome) > 2 and nome != " ":
        idade = int(input(f'Digite sua idade {nome}:'))
        print("Irei pesquisar filme para sua faxetaria de idade...")
        if idade >= 0 and idade < 10:
            filme1_10 = "1-Como treina o seu dragão" .upper()
            filme2_10 = "O Espanta Tubarões" .upper()
            filme3_10 = "Monstros S.A.".upper()
            escolha = int(input(f"Temos: \n1-{filme1_10}\n2-{filme2_10}\n3-{filme3_10}\n|>"))
            if escolha >= 3:
                print("")
            else:
                print("Digite um numero inteiro de 1 á 3 valido!!!")
                break
            print(f'Cliente: {nome}\nIdade: {idade}')
            if escolha == 3:
                print(f"Filme reservado: {filme3_10}")
            elif escolha == 2:
                print(f"Filme reservado: {filme2_10}")
            elif escolha == 1:
                print(f"Filme reservado: {filme1_10}")
        if idade >= 10 and idade < 18:
            filme1_18 = "Ted" .upper()
            filme2_18 = "A cabana".upper()
            filme3_18 = "Jogos Vorazes".upper()
            escolha = int(input(f"Temos: \n1-{filme1_18}\n2-{filme2_18}\n3-{filme3_18}\n|>"))
            if escolha >= 3:
                print("")
            else:
                print("Digite um numero inteiro de 1 á 3 valido!!!")
                break
            print(f'Cliente: {nome}\nIdade: {idade}')
            if escolha == 3:
                print(f"Filme reservado: {filme3_18}")
            elif escolha == 2:
                print(f"Filme reservado: {filme2_18}")
            elif escolha == 1:
                print(f"Filme reservado: {filme1_18}")
        print(f"\nAté mais {nome}!!!")
        break
    else:
        print("Digite o nome legivel!!")
        continue
