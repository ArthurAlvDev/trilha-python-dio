menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor depósito: "))

        if valor > 0:
            saldo += valor
        else:
            print("ERROR! Valor invalido!")

    elif opcao == "s":
        valor = float(input("Valor saque: "))

        if valor > saldo:
            print("ERROR! Saldo insuficiente.")

        elif valor > limite:
            print("ERROR! Limite insuficiente!")

        elif numero_saques >= LIMITE_SAQUES:
            print("ERROR! Sem limite de saque!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("ERROR! Valor invalido!")

    elif opcao == "e":
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("ERROR! Selecione Novamente!")
