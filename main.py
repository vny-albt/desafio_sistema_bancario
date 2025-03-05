saldo_atual = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = input("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => """)

    if menu == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo_atual += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido!")

    elif menu == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo_atual
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Número máximo de saques excedido!")

        elif valor > 0:
            saldo_atual -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("O valor informado é inválido!")

    elif menu == "3":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_atual:.2f}")

    elif menu == "4":
        break

    else:
        print("Por favor selecione novamente a operação desejada!")