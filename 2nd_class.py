class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0

    def deposit_cash(self, amount):
        if int(amount) < 0:
            print(f"Nie można dodawać do konta liczb ujemnych")
            return
        else:
            self.cash += amount
            return self.cash

    def withdraw_cash(self, amount):
        if self.cash < float(amount):
            print(f"za mało funduszy")
            return
        else:
            self.cash -= amount
    def print_info(self):
        print(f"numer konta:{self.number}\nstan konta: {self.cash}")


staszek = BankAccount(12)
staszek.deposit_cash(788)
staszek.print_info()
staszek.withdraw_cash(22)
staszek.print_info()



