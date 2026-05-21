# Expense Tracker Project

expenses = []
print("\n Welcome to Expense tracker")
while True:
    print("\n ======MENU======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Spending Category Wise")
    print("5. Exit")
    print("\n ================")

    choice = int(input("\n Please Enter Your Choice (1-5) : "))

    if choice == 1:
        date = input("Enter date (DD/MM/YYYY) : ")
        category = input("Enter category (Food/Travel/Clothes/etc... : ")
        description = input("Enter Short Description : ")
        amount = float(input("Enter Amount (₹) : "))

        expense = {
            "date" : date,
            "category" : category.capitalize(),
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("\n Your Expense Added Successfully")

    elif choice == 2:
        if len(expenses) == 0:
            print("\n No Expenses Added yet")
        else:
            i = 1
            for e in expenses:
                print(f"{i}. {e['date']} | {e['category']} | {e['description']} | {e['amount']}")
                i = i+1

    elif choice == 3:
        total = 0
        for e in expenses:
            total = total + e['amount']
        print(f"\nTotal Spending is :{total}")

    elif choice == 4:
        summary = {}
        for e in expenses:
            cat = e['category']
            if cat in summary:
                summary[cat] = summary[cat] + e['amount']
            else:
                summary[cat] = e['amount']
        print("\n Spending Category Wise\n")
        for cat, amt in summary.items():
            print(f"{cat}: ₹{amt}")

    elif choice == 5:
        print("\nThank You For Using Expense Tracker")
        break
    else:
        print("Invalid Choice Try Again")
        
