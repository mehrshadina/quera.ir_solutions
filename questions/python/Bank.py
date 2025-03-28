customers = {}

while True:
    command = input().strip().split()
    if not command:
        continue

    action = command[0].lower()
    
    if action == "exit":
        break

    elif action == "create" and len(command) == 3:
        accountId = command[1]
        initialBalance = int(command[2])
        if accountId in customers:
            print("Account already exists")
        else:
            customers[accountId] = initialBalance
            print("Account created successfully")

    elif action == "deposit" and len(command) == 3:
        accountId = command[1]
        amount = int(command[2])
        if accountId not in customers:
            print("Account does not exist")
        else:
            customers[accountId] += amount
            print("Deposit successful")

    elif action == "withdraw" and len(command) == 3:
        accountId = command[1]
        amount = int(command[2])
        if accountId not in customers:
            print("Account does not exist")
        else:
            if customers[accountId] < amount:
                print("Insufficient funds")
            else:
                customers[accountId] -= amount
                print("Withdraw successful")

    elif action == "balance" and len(command) == 2:
        accountId = command[1]
        if accountId not in customers:
            print("Account does not exist")
        else:
            print(customers[accountId])

    else:
        print("Invalid command")
