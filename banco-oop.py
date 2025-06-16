class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf})"

class ContaCorrente:
    def __init__(self, numero_conta, cliente, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.cliente = cliente  # A conta pertence a um cliente
        self.saldo = saldo_inicial
        self.historico_transacoes = [] # Para registrar depósitos e saques

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico_transacoes.append(f"Depósito: +R$ {valor:.2f}")
            return True
        else:
            print("❌ O valor do depósito deve ser positivo.")
            return False

    def sacar(self, valor):
        if valor <= 0:
            print("❌ O valor do saque deve ser positivo.")
            return False
        elif self.saldo >= valor:
            self.saldo -= valor
            self.historico_transacoes.append(f"Saque: -R$ {valor:.2f}")
            return True
        else:
            print("❌ Saldo insuficiente.")
            return False

    def exibir_saldo(self):
        print(f"💰 Saldo atual da conta {self.numero_conta}: R$ {self.saldo:.2f}")

    def exibir_historico(self):
        print(f"\n--- Histórico de Transações da Conta {self.numero_conta} ---")
        if not self.historico_transacoes:
            print("Nenhuma transação realizada ainda.")
        for transacao in self.historico_transacoes:
            print(transacao)
        print("------------------------------------------")

    def __str__(self):
        return f"Conta: {self.numero_conta} | Cliente: {self.cliente.nome} | Saldo: R$ {self.saldo:.2f}"

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = {}  # Dicionário para armazenar clientes por CPF
        self.contas = {}    # Dicionário para armazenar contas por número da conta
        self.proximo_numero_conta = 1001 # Inicia a numeração das contas

    def adicionar_cliente(self, nome, cpf):
        if cpf not in self.clientes:
            novo_cliente = Cliente(nome, cpf)
            self.clientes[cpf] = novo_cliente
            print(f"✅ Cliente '{nome}' (CPF: {cpf}) adicionado com sucesso.")
            return novo_cliente
        else:
            print(f"⚠️ Cliente com CPF {cpf} já existe.")
            return None

    def criar_conta(self, cpf_cliente, saldo_inicial=1000):
        cliente = self.clientes.get(cpf_cliente)
        if cliente:
            numero_conta = str(self.proximo_numero_conta)
            nova_conta = ContaCorrente(numero_conta, cliente, saldo_inicial)
            self.contas[numero_conta] = nova_conta
            self.proximo_numero_conta += 1
            print(f"✅ Conta corrente {numero_conta} criada para o cliente {cliente.nome}.")
            return nova_conta
        else:
            print(f"❌ Cliente com CPF {cpf_cliente} não encontrado. Por favor, adicione o cliente primeiro.")
            return None

    def buscar_conta(self, numero_conta):
        return self.contas.get(numero_conta)

    def menu_principal(self):
        print(f"\nBem-vindo ao {self.nome}!")
        while True:
            print("\n--- Menu Principal ---")
            print("1. Adicionar Cliente")
            print("2. Criar Conta Corrente")
            print("3. Acessar Conta")
            print("4. Sair")

            opcao_principal = input("Escolha uma opção: ")

            if opcao_principal == '1':
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente (somente números): ")
                self.adicionar_cliente(nome, cpf)

            elif opcao_principal == '2':
                cpf = input("Digite o CPF do cliente para criar a conta: ")
                self.criar_conta(cpf)

            elif opcao_principal == '3':
                numero_conta = input("Digite o número da conta para acessar: ")
                conta = self.buscar_conta(numero_conta)
                if conta:
                    self.menu_conta(conta)
                else:
                    print("❌ Conta não encontrada.")

            elif opcao_principal == '4':
                print("Obrigado por usar nosso sistema bancário. Até logo!")
                break
            else:
                print("❌ Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

    def menu_conta(self, conta):
        while True:
            print(f"\n--- Menu da Conta {conta.numero_conta} ({conta.cliente.nome}) ---")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Exibir Saldo")
            print("4. Exibir Histórico")
            print("5. Voltar ao Menu Principal")

            opcao_conta = input("Escolha uma opção: ")

            if opcao_conta == '1':
                try:
                    valor = float(input("Digite o valor para depositar: "))
                    conta.depositar(valor)
                except ValueError:
                    print("❌ Valor inválido. Por favor, digite um número.")

            elif opcao_conta == '2':
                try:
                    valor = float(input("Digite o valor para sacar: "))
                    conta.sacar(valor)
                except ValueError:
                    print("❌ Valor inválido. Por favor, digite um número.")

            elif opcao_conta == '3':
                conta.exibir_saldo()

            elif opcao_conta == '4':
                conta.exibir_historico()

            elif opcao_conta == '5':
                print("Voltando ao menu principal...")
                break
            else:
                print("❌ Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

# --- Executando o Sistema Bancário ---
if __name__ == "__main__":
    meu_banco = Banco("Meu Banco Digital S.A.")
    meu_banco.menu_principal()