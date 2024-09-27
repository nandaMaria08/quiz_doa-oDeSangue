nome = (input("Digite seu nome:"))

def menu():
    print("Menu de Verificação de Aptidão para Doação de Sangue:")
    print("1-Verificar aptidão")
    print("2-Sair")

    while True:
        escolha = input(nome + " digite o número da sua escolha, para sair ou verificar sua aptidão: ")
        if escolha == '1':
            verificar_aptidao()
        elif escolha == '2':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

def verificar_aptidao():
    print("Responda as perguntas a seguir com 'sim' ou 'não':")
    
    idade = input(nome + ",você tem entre 16 e 69 anos? ")
    peso = input(nome + ",você pesa mais de 50 kg? ")
    saude = input(nome + ",você está se sentindo bem hoje? ")
    
    if idade.lower() == 'sim' and peso.lower() == 'sim' and saude.lower() == 'sim':
        print(nome + ",você está apto(a) a doar sangue!")
    else:
        print(nome + ",você não está apto(a) a doar sangue no momento.")

menu()
