
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado para {self.titular}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado para {self.titular}")
        else:
            print("Saque não permitido")

    def saldo_atual(self):
        return self.saldo

class SistemaBancario:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        self.contas.append(conta)
        print(f"Conta criada para {titular} com saldo inicial de R$ {saldo_inicial}")

    def encontrar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        return None

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
        else:
            saida = []
            for conta in self.contas:
                saida.append(f"{conta.titular}: R$ {conta.saldo}")
            print(", ".join(saida))

# Instância do sistema bancário
sistema = SistemaBancario()

# Menu de opções
while True:
    print("\nMENU:")
    print("1 - Criar nova conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Listar contas")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        entrada = input("Digite o titular e o saldo inicial (Ex: João, 500): ").strip()
        try:
            titular, saldo = entrada.split(", ")
            sistema.criar_conta(titular, int(saldo))
        except:
            print("Entrada inválida. Tente novamente.")
    
    elif opcao == "2":
        titular = input("Digite o nome do titular: ").strip()
        conta = sistema.encontrar_conta(titular)
        if conta:
            try:
                valor = int(input("Digite o valor para depositar: ").strip())
                conta.depositar(valor)
            except:
                print("Valor inválido.")
        else:
            print("Conta não encontrada.")

    elif opcao == "3":
        titular = input("Digite o nome do titular: ").strip()
        conta = sistema.encontrar_conta(titular)
        if conta:
            try:
                valor = int(input("Digite o valor para sacar: ").strip())
                conta.sacar(valor)
            except:
                print("Valor inválido.")
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        sistema.listar_contas()

    elif opcao == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
