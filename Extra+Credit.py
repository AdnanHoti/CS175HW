#Adnan Hoti
#Extra Credit
def main():
    card_num = int(input('What is your BOA card number?'))
    card_num == 123
    val_card = validate_card_num(card_num)
    while val_card == False:
        print('The card number is invalid')
        card_num = int(input('What is your BOA card number?'))
        val_card = validate_card_num(card_num)

file = open("out.txt","w")
file.write("Transaction \t Balance \t Amount \t New Balance")
file.close()

balance = 0

def menu():
    print()
    print("Menu")
    print()
    print('Option 1: Deposit')
    print('Option 2: Withdraw')
    print('Option 3: Check Balance')
    print('Option 4: Print Transactions')
    print('Option 5: Print Statistics')
    print("Option 6: Exit")
    print()

def validate_card_num(card_num):
    if card_num < 1000 or card_num > 9999:
        return False
    else:
        return True
def validate_card_password(card_num, password_int):
    if password_int == str(card_num)[1:]:
        return True
    else:
        return False

def withdraw(price,balance):
    if price < 0:
        print('\nError: The amount is negative!')
    elif price > balance:
        print('\nError: The price is greater! ')
    else:
        print("\nSuccess!")
        balance -= price
    return balance

def show_balance(balance):
    print('\nYour balance:',balance)

def deposit(amount, balance):
    balance = balance+amount
    return balance

def save_transaction(filename, transaction,before_balance,amount,after_balance):
    file = open(filename,"a")
    file.writelines("\n" + transaction + " \t\t"  + before_balance + "\t\t " + amount +" \t\t " + after_balance)
    file.close()

def print_transactions(filename):
    file = open(filename,"r+")
    for line in file:
        print(line)
    file.close()

def print_statistics(filename):
    file = open(filename,"r+")
    valid_deposits = []
    valid_withdraws = []
    balances = []
    index2=0
    for line in file:
        if index2 == 0:
            index2+=1
        else:
            index2+=1
            lines = line.split("\t\t")
            action = lines[0]
            balance = lines[1]
            amount = float(lines[2])
            new_balance = float(lines[3])
            if action == "Deposit ":
                if amount >0:
                    valid_deposits.append(amount)
                    balances.append(balance)
            elif action == "Withdraw ":
                if new_balance>=0:
                    valid_withdraws.append(amount)
                    balances.append(balance)
    print("You have " + str(len(valid_deposits)) + " valid deposit transactions.")
    print("Your greatest depostit was $" + str(max(valid_deposits)) + ".")
    print("You have " + str(len(valid_withdraws)) + " valid withdraw transactions.")
    print("Your greatest withdraw was $" + str(max(valid_withdraws)) + ".")
    print("Overall, your largest account balance is $" + str(max(balances)) + " and smallest is $" + str(min(balances)) + ".")
    
    
file.close()
    

_menu = True
transaction = False
deposited = False
withdrawed = False

while _menu == True:
    menu()
    option = int(input('Choose an option: '))
    if option == 1:
        transaction = True
        deposited = True
        price = float(input('How much would you like to deposit? '))
        before_balance = balance
        balance = deposit(price, balance)
        save_transaction("out.txt", "Deposit", str(before_balance), str(price), str(balance))
    elif option == 2:
        transaction = True
        withdrawed = True
        price = float(input('How much do you want to withdraw? '))
        before_balance = balance
        balance = withdraw(price, balance)
        save_transaction("out.txt", "Withdraw", str(before_balance), str(price), str(balance))
    elif option == 3:
        show_balance(balance)
    elif option == 4:
        if transaction == False:
            print("You need to make a transaction first!")
            continue
        else:
            print_transactions("out.txt")
    elif option == 5:
        if transaction == False or deposited == False or withdrawed == False:
            print("You need to make one of each transaction first!")
            continue
        else:
            print_statistics("out.txt")
    elif option == 6:
        print('Goodbye! ')
        _menu = False
    else:
        print('This option is unavailable! ')
