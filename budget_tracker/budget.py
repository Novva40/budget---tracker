import json
import os

DATA_FILE = 'data.json'

# Load existing transactions or create an empty list
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save transactions to file
def save_data(transactions):
    with open(DATA_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)

# Add a transaction
def add_transaction(transactions):
    type_choice = input("Enter type (income/expense): ").strip().lower()
    if type_choice not in ['income', 'expense']:
        print("Invalid type. Must be 'income' or 'expense'.")
        return
    amount = float(input("Enter amount: $"))
    category = input("Enter category (e.g., food, rent, job): ").strip()
    note = input("Optional note: ").strip()

    transaction = {
        'type': type_choice,
        'amount': amount,
        'category': category,
        'note': note
    }
    transactions.append(transaction)
    save_data(transactions)
    print("✅ Transaction added!\n")

# View all transactions
def view_transactions(transactions):
    if not transactions:
        print("No transactions recorded.\n")
        return
    for i, t in enumerate(transactions, 1):
        print(f"{i}. {t['type'].title()} - ${t['amount']} [{t['category']}] {t['note']}")
    print()

# Show summary
def show_summary(transactions):
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expense = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    print(f"💰 Total Income: ${income}")
    print(f"💸 Total Expenses: ${expense}")
    print(f"📊 Balance: ${income - expense}\n")

# Delete Transaction Function
def delete_transaction(transactions):
    view_transactions(transactions)
    if not transactions:
        return
    try:
        index = int(input("Enter the number of the transaction to delete: ")) - 1
        if 0 <= index < len(transactions):
            removed = transactions.pop(index)
            save_data(transactions)
            print(f"❌ Deleted: {removed['type']} - ${removed['amount']} [{removed['category']}]\n")
        else:
            print("Invalid transaction number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# Edit Transaction Function
def edit_transaction(transactions):
    view_transactions(transactions)
    if not transactions:
        return
    try:
        index = int(input("Enter the number of the transaction to edit: ")) - 1
        if 0 <= index < len(transactions):
            transaction = transactions[index]
            print(f"Editing: {transaction['type']} - ${transaction['amount']} [{transaction['category']}] {transaction['note']}")
            
            # Edit amount
            amount = float(input("Enter new amount: $"))
            transaction['amount'] = amount
            
            # Edit category
            category = input("Enter new category (e.g., food, rent): ").strip()
            transaction['category'] = category
            
            # Edit note
            note = input("Enter new note: ").strip()
            transaction['note'] = note
            
            save_data(transactions)
            print(f"✅ Edited: {transaction['type']} - ${transaction['amount']} [{transaction['category']}] {transaction['note']}\n")
        else:
            print("Invalid transaction number.\n")
    except ValueError:
        print("Please enter a valid number.\n")    

# category summary
def category_summary(transactions):
    categories = {}
    
    # Loop through each transaction and sum by category
    for transaction in transactions:
        category = transaction['category']
        categories[category] = categories.get(category, 0) + transaction['amount']
    
    # Print the summary
    print("\n--- Category Summary ---")
    for category, total in categories.items():
        print(f"{category}: ${total:.2f}")

# Main menu loop
def main():
    transactions = load_data()

    while True:
        print("\n--- Budget Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Delete Transaction")
        print("5. Edit Transaction")
        print("6. Category Summary")
        print("7. Exit")  # New option
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            show_summary(transactions)
        elif choice == '4':
            delete_transaction(transactions)
        elif choice == '5':
            edit_transaction(transactions)
        elif choice == '6':
             category_summary(transactions)
        elif choice == '7':  # New choice
           print("Goodbye!")
           break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()