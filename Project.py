expenses = []
total_cost = 0.0

while True:
    print("\n---Expense Tracker---")
    print("1. Add expenses")
    print("2. Summary")
    print("3. Exit")

    choice = int(input("Choose one option(1-3):"))

    if choice == 1:
        items = input("What have you bought? ").capitalize()
        expenses.append(items)
        cost_type = int(input("Enter currency type\t1.Dollar\t2.Pkr(Choose 1 or 2):"))
        if cost_type != 1 and cost_type !=2:
                        print("Invalid choice! Please choose 1 or 2 and try again!")
                        continue
        cost = float(input("Enter currency value:"))
        if cost_type == 1:
            print(f"Added ${cost} for {items}")
            total_cost += cost*278
        elif cost_type == 2:
            print(f"Added Rs.{cost} for {items}")
            total_cost += cost


    elif choice == 2:
        print(expenses)
        print("Rs.",total_cost)
        print("$",total_cost/278)


    elif choice == 3:
        save = input("Would you like to save the data? (yes/no): ").lower()

        if save == "yes":                                    # saves the file to the default running folder
            file = open("external.txt", "a")

            file.write("Expenses:\n")
            for item in expenses:
                file.write(item + "\n")

            file.write(f"\nTotal in PKR: Rs {total_cost}\n")
            file.write(f"Total in USD: $ {total_cost / 278}\n")

            file.close()

            print("Data saved successfully in external.txt")

            print("Stay connected!")
            break
    else:
        print("Invalid choice!")