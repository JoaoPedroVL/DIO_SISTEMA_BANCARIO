# Simulando contas bancárias (dicionário)
contas = {
    "123456789": {
        "nome": "João Silva",
        "saldo": 1000.00,
        "limite_saque_diario": 500.00,
        "extrato": []
    },
    "987654321": {
        "nome": "Maria Gomes",
        "saldo": 500.00,
        "limite_saque_diario": 200.00,
        "extrato": []
    }
}

# Funções para operações bancárias
def criar_conta(nome, cpf, saldo_inicial, limite_saque_diario):
    # ... (implementação da função de criação de conta)

def depositar(numero_conta, valor):
    # ... (implementação da função de depósito)

def sacar(numero_conta, valor):
    # ... (implementação da função de saque)

def consultar_extrato(numero_conta):
    # ... (implementação da função de consulta de extrato)

# Menu principal e interação com o usuário
while True:
    print("\n--- Sistema Bancário ---")
    print("1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar Extrato")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        # Criar conta
        nome = input("Nome: ")
        cpf = input("CPF: ")
        saldo_inicial = float(input("Saldo inicial: "))
        limite_saque_diario = float(input("Limite de saque diário: "))
        criar_conta(nome, cpf, saldo_inicial, limite_saque_diario)
    elif opcao == "2":
        # Depositar
        numero_conta = input("Número da conta: ")
        valor = float(input("Valor do depósito: "))
        depositar(numero_conta, valor)
    elif opcao == "3":
        # Sacar
        numero_conta = input("Número da conta: ")
        valor = float(input("Valor do saque: "))
        sacar(numero_conta, valor)
    elif opcao == "4":
        # Consultar extrato
        numero_conta = input("Número da conta: ")
        consultar_extrato(numero_conta)
    elif opcao == "0":
        print("Obrigado por utilizar o Sistema Bancário!")
        break
    else:
        print("Opção inválida. Tente novamente.")
