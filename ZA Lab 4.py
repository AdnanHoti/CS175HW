is_choice_valid = True
windspeed_valid = True
loop = True
temp_fah = 34.6
temp_cel = (5/9) * (temp_fah-32)
wind_speed = 23
wind_direction = ''
user_input =input('What is the Weather Station Name?:')
print('\t'+user_input+' Weather Station')


def show_menu():
    print('Please select one of the following choices.')
    print('Option 1: Input')
    print('Option 2: Print')
    print('Option 3: Exit')

def input_weather():
    temp_fah = float(input('What is the current tempature(Fahrenheit)?:'))
    if temp_fah < -130 or temp_fah > 150:
        print('Invalid input!')
        temp_valid = False
    else:
        temp_cel = (5/9) * (temp_fah-32)
        
    
    wind_speed = int(input('What is the wind speed?:'))
    if wind_speed < 0:
        print('The input wind speed is invalid!')
        windspeed_valid = False
    
    wind_direction = input('What is wind direction?:')
    return wind_speed, temp_fah, wind_direction

def print_weather(temp_f,wind_speed,wind_direction):
    print(" Temp: " + str(temp_f) + " Wind Speed: " + str(wind_speed) + " Wind Direction " + wind_direction)

def valid_choice(choice):
    if choice == '1' or choice == '2' or choice =='3':
        return True
    else:
        return False


inputed = False
while loop == True:
    show_menu()
    option_input = input('What is your choice? ')
    valid = valid_choice(option_input)
    if valid == True:
        if (option_input == '1'):
            inputed = True
            readings = input_weather()
            temp_fah=readings[1]
            wind_speed=readings[0]
            wind_direction=readings[2]
        elif (option_input == '2'):
            if inputed == True:
                print_weather(temp_fah, wind_speed, wind_direction)
            else:
                print("No weather entered. Visit option 1 first.")
                continue
        elif (option_input == '3'):
            print("Goodbye!")
            loop = False
    elif valid == False:
        print("Invalid!")
        continue
