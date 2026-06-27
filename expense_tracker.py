# Expense Tracker Project

expenses = []

def add_expense():
    item = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((item, amount))
    print("Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses added yet.\n")
    else:
        print("\nYour Expenses:")
        total = 0
        for item, amount in expenses:
            print(f"{item} : Rs.{amount}")
            total += amount
        print("Total Expense = Rs.", total)
        print()

while True:
    print("===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")
