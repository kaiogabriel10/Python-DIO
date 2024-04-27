class bank():
    def __init__(self,nome,numero_conta):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = 0
        self.conta = 0
    
    def verSaldo(self):
        print(f"Seu saldo é de {self.saldo}R$")
    
    def Depositar(self):
        print(f"Seu saldo é de {self.saldo}R$.")
        valor_deposito = float(input("Digite o valor de deposito:"))
        if valor_deposito < 100:
            print("Não é possível deposítar esse valor, Tente Novamente.")
            valor_deposito = float(input("Digite o valor do deposito: "))
        else:
            self.saldo+=valor_deposito
            print(f"O valor de {valor_deposito}R$ foi deposítado a sua conta.")

    def Sacar(self):
        print(f"Seu saldo é de {self.saldo}R$.")
        valor_saque = float(input("Digite o valor do saque: "))
        if self.saldo <= 0:
            print("Você não tem este valor deseja usar os creditos [Y/N].")
            decision = input("").upper
            if decision == "Y":
                print("Você usou seus créditos.")
                self.conta+=valor_saque
            else:
                print("Você não possui saldo o suficiente")

        else:
            valor_saque = float(input("Digite o valor do saque: "))
            self.saldo-=valor_saque
            print(f"O valor de {valor_saque} foi debitado da sua conta.")

    def verConta(self):
        print(f"Você devera pagar o valor de {self.conta}")


conta1 = bank("Maria",3333)
conta1.verSaldo()
conta1.Depositar()
conta1.verSaldo()