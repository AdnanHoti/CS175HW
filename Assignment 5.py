#Adnan Hoti
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
    print('Option 5: Exit')
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
    file.writelines("\n" + transaction + " \t\t"  + before_balance + " \t " + amount +" \t\t " + after_balance)
    file.close()

def print_transactions(filename):
    file = open(filename,"r+")
    for line in file:
        print(line)
    file.close()
    
'''
print('Welcome to BOA!')
password_int = input('\n What is your password?:')
entered = 1
val_pass = False
while val_pass == False:
    print('Your password is incorrect!')
    entered +=1
    if entered == 3:
        print('\nYour card is locked now.')
        print('Goodbye!')
        exit()
    else:
        continue
else:
    print('You have this amount tries left:', 3-entered)
    password_int = input('Enter ur BOA passcode:')
    entered += 1
    card_num = 123
    val_pass = validate_card_password(card_num, password_int)'''

_menu = True
transaction = False

while _menu == True:
    menu()
    option = int(input('Choose an option: '))
    if option == 1:
        transaction = True
        price = float(input('How much would you like to deposit? '))
        before_balance = balance
        balance = deposit(price, balance)
        save_transaction("out.txt", "Deposit", str(before_balance), str(price), str(balance))
    elif option == 2:
        transaction = True
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
        print('Goodbye! ')
        _menu = False
    else:
        print('This option is unavailable! ')
