# crud accounts.

accounts_list = [None] * 4
file_name = "accounts.txt"

def open_an_account():
    accounts_list[0] = input("Enter customer account number: ")
    accounts_list[1] = input("Enter customer name: ")
    accounts_list[2] = int(input("Enter balance amount: "))
    accounts_list[3] = 'A'
    fp_accounts = open(file_name, "a")
    fp_accounts.write(",".join(map(str, accounts_list)) + "\n")
    fp_accounts.close()
    print("Record created successfully")

def show_all_records():
    found = False
    fp_accounts = open(file_name, "r")
    print("account number   name    balance  status")
    for line in fp_accounts:
        found = True
        account_number, name, balance, status = line.strip().split(",")
        print(account_number, "            ", name, "     ", balance, "    ", status)
    fp_accounts.close()
    if not found:
        print("No records found")

def read_all_records():
    records = []
    fp_accounts = open(file_name, "r")
    for line in fp_accounts:
        records.append(line.strip().split(","))
    return records

def find_record(records):
    acc_number = input("Enter account number: ")
    for index, record in enumerate(records):
        if record[0] == acc_number:
            return index
    return -1

def write_all_records(records):
    fp_accounts = open(file_name, "w")
    for record in records:
        fp_accounts.write(",".join(record) + "\n")
    return True
    
def withdraw():
    records = read_all_records()
    index = find_record(records)
    if index == -1:
        print("Record not found. ")
        return
    withdraw_amount = int(input("Enter amount to withdraw: "))
    balance = int(records[index][2])
    if withdraw_amount > balance:
        print("Insufficient balance.")
        return
    records[index][2] = str(balance - withdraw_amount)
    result = write_all_records(records)
    if result:
        print("Withdrawl successful.")

def deposit():
    records = read_all_records()
    index = find_record(records)
    if index == -1:
        print("Record not found.")
        return
    deposit_amount = int(input("Enter amount to deposit: "))
    balance = int(records[index][2])
    records[index][2] = str(balance + deposit_amount)
    result = write_all_records(records)
    if result:
        print("Deposit successful.")

def close_an_account():
    records = read_all_records()
    index = find_record(records)
    if index == -1:
        print("Record not found.")
        return
    records[index][3] = 'C'
    result = write_all_records(records)
    if result:
        print("Record deleted successfully!")
    
def main():
    user_option = 1

    while user_option == 1:
        print("\n1. Open an Account")
        print("2. Show all Records")
        print("3. Withdraw")
        print("4. Deposit")
        print("5. Close an Account")
        print("6. Exit")
        print("------------------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            open_an_account()
        elif choice == 2:
            show_all_records()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            deposit()
        elif choice == 5:
            close_an_account()
        elif choice == 6:
            user_option = 0


if __name__ == "__main__":
    main()

