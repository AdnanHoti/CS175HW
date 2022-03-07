#Adnan Hoti
def main():
    card_num = int(input('What is your BOA card number?'))
    card_num == 123
    val_card = validate_card_num(card_num)
    while val_card == False:
        print('The card number is invalid')
        card_num = int(input('What is your BOA card number?'))
        val_card = validate_card_num(card_num)
    

print('Welcome to BOA!')

password_int = input('\n What is your password?:')
entered = 1

while val_pass == False:
    print('Your password is incorrect!')
    if entered == 3:
        print('\nYour card is locked now.')
        print('Goodbye!')
        exit()
else:
    print('You have this amount tries left:', 3-entered)
    password_int = input('Enter ur BOA passcode:')
    entered += 1
    val_pass = validate_card_pass(card_num, password_int)

_menu = True
total = 0

while _menu == True:
    menu()
    option = int(input('Choose an option 1:'))
    option = int(input('Choose an option 2:'))
    option = int(input('Choose an option 3:'))
    option = int(input('Choose an option 4:'))

if option == 1:
    price = float(input('How much would you like to deposit?'))
    total = deposit(total, price)
elif option == 2:
    price = float(input('How much do you want to withdraw?'))
    total = withdraw(total, price)
elif option == 3:
    show_balance(balance)
elif option == 4:
    print('Goodbye!')
else:
    print('This option is unavailable!')
    menu()
    option = int(input('Please enter option (1,2,3,4):'))
def menu():
    print('Option 1: Deposit')
    print('Option 2: Withdraw')
    print('Option 3: Check Balance')
    print('Option 4: Exit')
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

def withdraw(balance,price):
    if price < 0:
        print('The amount is negative!')
        print('The transaction is complete!')
        
    elif price > balance:
        print('the price is greater!')
        print('The transaction is complete!')
    else:
        balance += price
    return balance

def show_balance(balance):
    print('Your balance:',balance)
        

    

    
                
                
            
            
