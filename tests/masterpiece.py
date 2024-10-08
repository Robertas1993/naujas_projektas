from naujas_projektas.Budget_beta.budget import Budget
budget = Budget()

while True:
    print("\n1 - Enter income")
    print("2 - Enter expenses")
    print("3 - Get balance")
    print("4 - Display report")
    print("5 - Delete record")
    print("9 - Exit program")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        try:
            amount = float(input("Enter income amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        sender = input("Enter sender: ")
        additional_info = input("Enter additional info: ")
        try:
            budget.add_income_record(amount, sender, additional_info)
            budget.get_balance()
            budget.display_report()
        except Exception as error:
            print(f"Error: {error}")
    elif choice == 2:
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        payment_method = input("Enter payment method: ")
        purchased_item_service = input("Enter purchased item/service: ")
        try:
            budget.add_expense_record(amount, payment_method, purchased_item_service)
            budget.get_balance()
            budget.display_report()
        except Exception as error:
            print(f"Error: {error}")
    elif choice == 3:
        try:
            budget.get_balance()
        except Exception as error:
            print(f"Error: {error}")
    elif choice == 4:
        try:
            budget.display_report()
        except Exception as error:
            print(f"Error: {error}")
            
    elif choice == 5:

        try:
            budget.display_report()
            index = int(input("Enter the index of the record to delete: "))
            budget.delete_record(index - 1)
            budget.display_report()
        except Exception as error:

            print(f"Error: {error}")
    elif choice == 9:
        print("Bankruptcy liquidation has been initiated....")
        break
    else:
        print("Invalid choice. Please try again.")