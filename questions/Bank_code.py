class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, accountId, initialBalance=0):
        if accountId in self.customers:
            print("Account already exists")
        else:
            self.customers[accountId] = initialBalance
            print("Account created successfully")

    def deposit(self, accountId, amount):
        if accountId not in self.customers:
            print("Account does not exist")
        else:
            self.customers[accountId] += amount
            print("Deposit successful")

    def withdraw(self, accountId, amount):
        if accountId not in self.customers:
            print("Account does not exist")
        elif self.customers[accountId] < amount:
            print("Insufficient funds")
        else:
            self.customers[accountId] -= amount
            print("Withdraw successful")

    def get_balance(self, accountId):
        if accountId not in self.customers:
            print("Account does not exist")
        else:
            print(self.customers[accountId])

bank = Bank()
while True:
    command = input().strip().split()
    if command[0] == "exit":
        break
    elif command[0] == "create":
        accountId = command[1]
        initialBalance = int(command[2])
        bank.create_account(accountId, initialBalance)
    elif command[0] == "deposit":
        accountId = command[1]
        amount = int(command[2])
        bank.deposit(accountId, amount)
    elif command[0] == "withdraw":
        accountId = command[1]
        amount = int(command[2])
        bank.withdraw(accountId, amount)
    elif command[0] == "balance":
        accountId = command[1]
        bank.get_balance(accountId)
