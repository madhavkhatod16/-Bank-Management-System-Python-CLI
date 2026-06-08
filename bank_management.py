accounts = {}

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")

        accounts[acc_no] = {
            "name": name,
            "balance": 0
        }

        print("Account Created Successfully!")

    elif choice == "2":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            amount = float(input("Enter Deposit Amount: "))

            accounts[acc_no]["balance"] += amount

            print("Deposit Successful!")
            print("Balance:", accounts[acc_no]["balance"])

        else:

            print("Account Not Found!")

    elif choice == "3":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            amount = float(input("Enter Withdraw Amount: "))

            if amount <= accounts[acc_no]["balance"]:

                accounts[acc_no]["balance"] -= amount

                print("Withdrawal Successful!")
                print("Balance:", accounts[acc_no]["balance"])

            else:

                print("Insufficient Balance!")

        else:

            print("Account Not Found!")

    elif choice == "4":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            print("Balance:", accounts[acc_no]["balance"])

        else:

            print("Account Not Found!")

    elif choice == "5":

        acc_no = input("Enter Account Number: ")

        if acc_no in accounts:

            print("\nAccount Number:", acc_no)
            print("Name:", accounts[acc_no]["name"])
            print("Balance:", accounts[acc_no]["balance"])

        else:

            print("Account Not Found!")

    elif choice == "6":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")
