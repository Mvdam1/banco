def sistema_bancario():
    saldo = 1000  # Saldo inicial de R$ 1000

    while True:
        print("\n--- Menu do Banco ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Saldo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                valor_deposito = float(input("Digite o valor para depositar: "))
                if valor_deposito > 0:
                    saldo += valor_deposito
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")
                else:
                    print("O valor do depósito deve ser positivo.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

        elif opcao == '2':
            try:
                valor_saque = float(input("Digite o valor para sacar: "))
                if valor_saque > 0:
                    if saldo >= valor_saque:
                        saldo -= valor_saque
                        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("O valor do saque deve ser positivo.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

        elif opcao == '3':
            print(f"Seu saldo atual é de R$ {saldo:.2f}")

        elif opcao == '4':
            print("Obrigado por usar nosso sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

# Iniciar o sistema bancário
sistema_bancario()