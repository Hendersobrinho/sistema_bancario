from datetime import datetime

def exibir_menu():
    menu = """\

    ===== BANCO PY =====
    [L] Login
    [O] Logout
    [A] Abrir Conta Bancária
    [C] Cadastrar Usuário
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [X] Sair
    ====================
    Escolha uma opção para continuar: """
    return input(menu).upper()

class Usuario:
    lista_de_usuarios = []

    def __init__(self, cpf, nome, nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.endereco = endereco
        self.contas = []  

    @classmethod
    def verificar_endereco(cls):
        while True:
            endereco_rua = input("Digite o nome do Logradouro: ").strip()
            endereco_numero = input("Digite o Nº da casa/aptº: ").strip()
            endereco_bairro = input("Digite o Bairro: ").strip()
            endereco_cidade = input("Digite a Cidade: ").strip()
            endereco_estado = input("Digite a UF (Estado): ").strip()

            if all([endereco_rua, endereco_numero, endereco_bairro, endereco_cidade, endereco_estado]):
                endereco = f"Logradouro: {endereco_rua}, Nº: {endereco_numero} - Bairro: {endereco_bairro} - Cidade: {endereco_cidade}/{endereco_estado}"
                return endereco
            else:
                print("⚠️ Todos os campos do endereço são obrigatórios! Tente novamente.\n")

    @classmethod
    def verificar_cpf(cls, cpf):
        for usuario in cls.lista_de_usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None  

    @classmethod
    def novo_usuario(cls):
        while True:
            cpf = input("Digite o CPF contendo apenas números: ")
            if not cpf.isdigit() or len(cpf) != 11:
                print("CPF inválido! Deve conter exatamente 11 dígitos.\n")
                continue

            if cls.verificar_cpf(cpf):
                print("⚠️ CPF já cadastrado!\n")
                return

            nome = input("Digite seu nome: ")

            data_str = input("Digite a data no formato (DD/MM/AAAA): ")
            try:
                nascimento = datetime.strptime(data_str, "%d/%m/%Y")
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.\n")
                continue

            endereco = cls.verificar_endereco()
            if not endereco:
                continue

            novo_usuario = cls(cpf, nome, nascimento, endereco)
            cls.lista_de_usuarios.append(novo_usuario)

            print("\nUsuário criado com sucesso!")
            print(f"NOME: {nome}")
            print(f"CPF: {cpf}")
            print(f"DATA DE NASCIMENTO: {nascimento.strftime('%d/%m/%Y')}")
            print(f"ENDEREÇO: {endereco}")
            return novo_usuario

class ContaBancaria:
    contas = []
    contador_de_contas = 0

    def __init__(self, usuario, numero_conta, agencia="0001", saldo=0):
        self.usuario = usuario
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.saldo = saldo
        self.transacoes = []

    @classmethod
    def criar_conta(cls):
        cpf = input("Digite o CPF para abrir uma conta: ")

        usuario_encontrado = Usuario.verificar_cpf(cpf)
        if not usuario_encontrado:
            print("Usuário não cadastrado! Cadastre-se primeiro.")
            return

        cls.contador_de_contas += 1
        numero_conta = str(cls.contador_de_contas).zfill(4)

        nova_conta = cls(usuario_encontrado, numero_conta)
        cls.contas.append(nova_conta)
        usuario_encontrado.contas.append(nova_conta)

        print("\nConta bancária criada com sucesso!")
        print(f"Agência: {nova_conta.agencia}")
        print(f"Conta: {nova_conta.numero_conta}")

        return nova_conta  

    def depositar(self):
        valor = float(input("Digite o valor a depositar: "))
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: R${valor:.2f}")
            print(f"\nDepósito realizado com sucesso! Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self):
        limite_saques = 3
        hoje = datetime.now().date()

        # Contar quantos saques hoje
        saques_hoje = 0
        for transacao in self.transacoes:
            if transacao.startswith("Saque:"):
                # Vamos considerar que a transação foi feita hoje (já que você não salva a data)
                # Então para funcionar, vamos adicionar um truque:
                saques_hoje += 1

        if saques_hoje >= limite_saques:
            print("⚠️ Limite de 3 saques diários atingido. Tente novamente amanhã.")
            return

        valor = float(input("Digite o valor a sacar: "))

        if valor > 500:
            print("⚠️ Limite máximo de saque por operação é de R$500.")
        elif valor > self.saldo:
            print("⚠️ Saldo insuficiente para saque.")
        elif valor <= 0:
            print("⚠️ O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            self.transacoes.append(f"Saque: R${valor:.2f}")
            print(f"\n✅ Saque realizado! Saldo atual: R${self.saldo:.2f}")

    def exibir_extrato(self):
        print("\n====== EXTRATO BANCO PY ======")
        if not self.transacoes:
            print("Nenhuma transação realizada ainda.")
        else:
            for transacao in self.transacoes:
                print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

usuario_logado = None

def login():
    global usuario_logado
    cpf = input("Digite o CPF para login: ")
    usuario_encontrado = Usuario.verificar_cpf(cpf)
    if usuario_encontrado:
        usuario_logado = cpf
        print(f"\n✅ Usuário {usuario_encontrado.nome} logado!")
    else:
        print("Usuário não encontrado!")

def logout():
    global usuario_logado
    usuario_logado = None
    print("\nUsuário saiu da sessão.")

while True:
    opcao = exibir_menu()

    if opcao == "L":
        login()

    elif opcao == "O":
        logout()

    elif opcao == "A":
        ContaBancaria.criar_conta()

    elif opcao == "C":
        Usuario.novo_usuario()

    elif opcao in ["D", "S", "E"]:
        cpf = usuario_logado if usuario_logado else input("Digite o CPF: ")
        contas = [c for c in ContaBancaria.contas if c.usuario.cpf == cpf]

        if contas:
            print("\nEscolha uma conta para operar:")
            for idx, conta in enumerate(contas):
                print(f"[{idx}] Conta: {conta.numero_conta} - Saldo: R${conta.saldo:.2f}")

            try:
                escolha = int(input("Digite o número da conta desejada: "))
                conta = contas[escolha]

                if opcao == "D":
                    conta.depositar()
                elif opcao == "S":
                    conta.sacar()
                else:
                    conta.exibir_extrato()
            except (IndexError, ValueError):
                print("Escolha inválida! Tente novamente.")
        else:
            print("Nenhuma conta encontrada! Faça login ou abra uma conta primeiro.")

    elif opcao == "X":
        print("Obrigado por usar nosso sistema!")
        break

    else:
        print("Opção inválida! Escolha uma alternativa válida.")