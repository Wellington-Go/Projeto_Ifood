Banco = """
        [d] Deposito
        [s] Saque
        [e] Extrato
        [q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True: # Inicio da estrutura de relacional

    opcao = input(Banco)# Inicio do código.

    if opcao == 'd':
       valor = float(input(' Informe o valor do depósito: '))
       if valor > 0:
           saldo += valor
           extrato += f"Deposito: R${valor:.2f}\n"
       else:
           print(' Operaçao falhou ! o valor informado e inválido.')

    elif opcao == 's':
        valor = float(input(' Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque

        # Inicio da validação se excedeu o saldo, limite ou saque.

        if excedeu_saldo:
            print(' Operação falhou! voce não tem saldo suficiente.')
        elif excedeu_limite:
            print(' Operação falhou! o valor do saque e maior. ')
        elif excedeu_saques:
            print(' Operação falho! numero máximo de saques excedido. ')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
        else:
            print(' Operação falho! o valor informado e inválido! ')

    elif opcao == 'e':
        print("\n========== EXTRATO ==========")
        print(' Não foi realizado movimentação.'if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('================================')

    elif opcao == 'q':
        break
    else:
        print(' Operação invalida! selecione a opção correta. ')

print('Encerrado!') # Final do código.
