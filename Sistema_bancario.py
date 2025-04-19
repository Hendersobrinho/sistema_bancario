def exibir_menu(): #Funcao para chamar o menu
    menu = """\
    \n
    ===== BANCO PY =====
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [X] Sair
    ====================
    Escolha uma opção para continuar: """
    return input(menu).upper()


saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

def depositar(): 

    global saldo, extrato #Habilitando as variáveis globais dentro da função

    print("Depositar")
    
    while True:
        try:
            valor = float(input("Digite o valor a depositar: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: +R${valor:.2f}\n"
                print (f"Depósito realizado com sucesso!\nSeu saldo agora é: R${saldo:.2f}")
                break
            else:
                print("Recusado! O valor do depósito deve ser maior que zero")

        except ValueError:
            print("Entrada inválida, digite um número válido")
        
def sacar():

    global saldo, extrato, numero_de_saques, limite, LIMITE_DE_SAQUES #Habilitando as variáveis globais dentro da função

    print("Sacar")
    
    while True:
        try:
            valor_saque = float(input("Digite o valor do saque: "))       
                 
            if valor_saque > saldo: #primeiro verificando as condições que não permitem o saque.
                print("Saldo insuficiente!")
            elif numero_de_saques >= LIMITE_DE_SAQUES:
                print ("Limite de saques diário atingido")
                return
            elif valor_saque > limite:
                print (f"Saque realizado deve ser no máximo de R${limite:.2f}")
            else: #Depois de verificar se estar apto ao saque, realizando o saque.
                saldo -= valor_saque
                numero_de_saques += 1 #Adicionar 1 a contagem de saques
                extrato += f"Saque: -R${valor_saque:.2f}\n"
                print (f"Saque realizado com sucesso!\nSeu saldo agora é: R${saldo:.2f}")

                break
        except ValueError:
            print("Entrada inválida, digite um número válido")


def exibir_extrato():
    global extrato, saldo

    print("\n====== EXTRATO BANCO PY ======")
    print(extrato if extrato else "Nenhuma Movimentação realizada")
    print(f"Saldo atual: R${saldo:.2f}")


while True:
    opcao = exibir_menu()
    
    if opcao == "D":
        depositar()
    elif opcao == "S":
        sacar()
    elif opcao == "E":
        exibir_extrato()
    elif opcao == "X":
        print("Obrigado por usar nosso sistema!")
        input("Pressione enter para sair ")
    
        break
    
    else:
        print("Opção inválida! Escolha uma das alternativas")





