def criar_conta(nome, cpf, saldo_inicial, limite_saque_diario, taxa_saque=0):
    if saldo_inicial < 50:
        print("Saldo inicial deve ser maior ou igual a R$ 50,00.")
        return

    nova_conta = {
        "nome": nome,
        "saldo": saldo_inicial,
        "limite_saque_diario": limite_saque_diario,
        "taxa_saque": taxa_saque,
        "extrato": []
    }
    contas[cpf] = nova_conta
    print(f"Conta criada com sucesso para {nome} (CPF: {cpf})!")

def depositar(numero_conta, valor):
    if valor <= 0:
        print("Valor inválido para depósito.")
        return

    conta = get_conta(numero_conta)
    if not conta:
        print(f"Conta {numero_conta} não encontrada.")
        return

    conta["saldo"] += valor
    registrar_transacao(numero_conta, "Depósito", valor)
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {numero_conta}.")

def sacar(numero_conta, valor):
    if valor <= 0:
        print("Valor inválido para saque.")
        return

    conta = get_conta(numero_conta)
    if not conta:
        print(f"Conta {numero_conta} não encontrada.")
        return

    if valor > conta["saldo"]:
        print("Saldo insuficiente para saque.")
        return

    if valor > conta["limite_saque_diario"]:
        print("Valor excede o limite de saque diário.")
        return

    taxa = valor * conta["taxa_saque"]
    valor_sacado = valor + taxa
    conta["saldo"] -= valor_sacado
    registrar_transacao(numero_conta, "Saque", valor, taxa)
    print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {numero_conta}.")
    print(f"Taxa de saque: R$ {taxa:.2f}")

def consultar_extrato(numero_conta):
    conta = get_conta(numero_conta)
    if not conta:
        print(f"Conta {numero_conta} não encontrada.")
        return

    extrato = conta["extrato"]
    if not extrato:
        print(f"Conta {numero_conta} ainda não possui movimentações.")
        return

    print("\n--- Extrato da Conta", numero_conta, "---")
    for transacao in extrato:
        print(f"{transacao['data']:.20s} | {transacao['tipo']:8s} | R$ {transacao['valor']:8.2f} | {transacao.get('taxa', 0):8.2f}")

def get_conta(numero_conta):
    return contas.get(numero_conta)

def registrar_transacao(numero_conta, tipo, valor, taxa=0):
    conta = get_conta(numero_conta)
    transacao = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "valor": valor,
        "taxa": taxa
    }
    conta["extrato"].
