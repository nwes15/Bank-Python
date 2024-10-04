class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido. Não é possível depositar valores negativos.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor inválido. Não é possível sacar valores negativos ou zero.")

    def mostrar_extrato(self):
        if self.extrato:
            print("\nExtrato bancário:")
            for operacao in self.extrato:
                print(operacao)
            print(f"\nSaldo atual: R${self.saldo:.2f}")
        else:
            print("Nenhuma operação realizada até o momento.")
        print("\n-----------------------")

def menu():
    banco = Banco()
    
    while True:
        print("\nOpções:")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver Extrato")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        # Verifica se a opção é um número válido
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 1:
                try:
                    valor = float(input("Informe o valor para depósito: R$"))
                    banco.depositar(valor)
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            
            elif opcao == 2:
                try:
                    valor = float(input("Informe o valor para saque: R$"))
                    banco.sacar(valor)
                except ValueError:
                    print("Por favor, insira um valor numérico válido.")
            
            elif opcao == 3:
                banco.mostrar_extrato()
            
            elif opcao == 4:
                print("Saindo do sistema bancário.")
                break
            
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Por favor, escolha uma opção numérica válida.")

# Executar o sistema bancário
menu()
