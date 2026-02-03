 # crud accounts.

file_name = "accounts.dat"
accounts = []
want_to_exit = 1

def main():
    global accounts
    accounts = load_accounts()

    while want_to_exit == 1:
        print("\n1. Open an Account")
        print("2. Show all accounts")
        print("3. update an account")         
        print("4. Close an Account")
        print("5. Exit")
        print("------------------------------------")

        choice = int(input("Enter your choice: "))
        options = [open_an_account, show_all_accounts, update_an_account, close_an_account, exit]
        options[choice - 1]()

def open_an_account():
    account_number = input("Enter account number: ")
    name = input("Enter customer name: ")
    balance = int(input("Enter the customer balance: "))
    status = 'A'
    account = [account_number, name, balance, status]
    accounts.append(account)
    save_accounts(accounts)
    operation = "opened"
    print_response(operation)

def show_all_accounts():
    if accounts:
        print("acc number\tname\tbalance\tstatus")
        for account in accounts:
            print(account[0], "\t\t", account[1], "\t", account[2], "\t", account[3])
    else:
        print("No accounts found! ")

def find_record(account_number):
    for account in accounts:
        if account[0] == account_number:
            return account
    print("Account not found! ")
    return []

def update_an_account():
    account_number = input("Enter account number to update: ")
    account = find_record(account_number)
    if account:
        account[2] = int(input("Enter balance to update: "))
        save_accounts(accounts)
        operation = "updated"
        print_response(operation)
   
def close_an_account():
    permission = input("Are you sure! you want exit enter y otherwise enter n")
    if permission == 'y':
        account_number = input("Enter account number to delete: ")
        account = find_record(account_number)
        if account:
            account[3] = 'C'
            save_accounts(accounts)
        operation = "closed"
        print_response(operation)

def load_accounts():
    with open(file_name, "r") as accounts_file:
        accounts = accounts_file.read()
        if accounts:
            return eval(accounts)
        return []

def save_accounts(accounts):
    with open(file_name, "w") as accounts_file:
        accounts_file.write(str(accounts))

def print_response(operation):
    print("account", operation, "successfully! ")

def exit():
    global want_to_exit
    want_to_exit = 0
        
if __name__ == "__main__":
    main()

