accounts = {}

def get_input(message):
    value = input(message)

    if value.lower() == "exit":
        print("Thank You!")
        exit()

    return value


while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = get_input("Enter Choice: ")

    if choice == "1":

        acc_no = get_input("Enter Account Number: ")

        if acc_no in accounts:
            print("Account Already Exists!")

        else:
            name = get_input("Enter Name: ")
            pin = get_input("Create 4-Digit PIN: ")

            accounts[acc_no] = {
                "name": name,
                "pin": pin,
                "balance": 0
            }

            print("Account Created Successfully!")

    elif choice == "2":

        acc_no = get_input("Enter Account Number: ")
        pin = get_input("Enter PIN: ")

        if acc_no in accounts and accounts[acc_no]["pin"] == pin:

            amount = float(get_input("Enter Deposit Amount: "))

            accounts[acc_no]["balance"] += amount

            print("Deposit Successful!")
            print("Current Balance:", accounts[acc_no]["balance"])

        else:
            print("Invalid Account Number or PIN!")

    elif choice == "3":

        acc_no = get_input("Enter Account Number: ")
        pin = get_input("Enter PIN: ")

        if acc_no in accounts and accounts[acc_no]["pin"] == pin:

            amount = float(get_input("Enter Withdrawal Amount: "))

            if amount <= accounts[acc_no]["balance"]:

                accounts[acc_no]["balance"] -= amount

                print("Withdrawal Successful!")
                print("Remaining Balance:", accounts[acc_no]["balance"])

            else:
                print("Insufficient Balance!")

        else:
            print("Invalid Account Number or PIN!")

    elif choice == "4":

        acc_no = get_input("Enter Account Number: ")
        pin = get_input("Enter PIN: ")

        if acc_no in accounts and accounts[acc_no]["pin"] == pin:

            print("Current Balance:",
                  accounts[acc_no]["balance"])

        else:
            print("Invalid Account Number or PIN!")

    elif choice == "5":

        acc_no = get_input("Enter Account Number: ")
        pin = get_input("Enter PIN: ")

        if acc_no in accounts and accounts[acc_no]["pin"] == pin:

            print("\n===== ACCOUNT DETAILS =====")
            print("Account Number :", acc_no)
            print("Name           :", accounts[acc_no]["name"])
            print("Balance        :", accounts[acc_no]["balance"])

        else:
            print("Invalid Account Number or PIN!")

    elif choice == "6":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")
