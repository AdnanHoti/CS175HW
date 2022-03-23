is_choice_valid = True
windspeed_valid = True
loop = True
temp_fah = 34.6
temp_cel = (5/9) * (temp_fah-32)
wind_speed = 23

user_input =input('What is the Weather Station Name?:')
print('\t'+user_input+' Weather Station')

print('Please select one of the following choices.')
option_input = print('Option 1: Input')
option_input = print('Option 2: Print')
option_input = print('Option 3: Exit')

option_input = ('What is your choice')
                       
while loop == True:
    if (option_input == 1):
        input_weather = input('\n Input weather reading? (y/Y for yes, n/N for no):')
    if input_weather == 'no':
        print('Goodbye!')
    elif input_weather == 'yes':
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

input_weather = input('\n Output the weather reading? (y/Y for yes, n/N for no):')

if input_weather == 'no':
    print('Goodbye!')

elif input_weather == 'yes':
    print('\t'+user_input+' Weather Station')

if is_choice_valid == True:
    print_weather(temp_f,wind_speed,wind_direction)
    print(f'{"Tempature(Fahrenheit):":>30}', f'{temp_fah:,.1f}')
    print(f'{"Tempature(Celcius):":>30}', f'{temp_cel:,.1f}')
else:
    print(f'{"Tempature(Fahrenheit):":>30}', f'{temp_fah:,.1f} error')
    print(f'{"Tempature(Celcius):":>30}', f'{temp_cel:,.1f} error')

    
if windspeed_valid == True:
    print(f'{"Wind Speed(mph):":>30}', wind_speed)
else:
    print("error")
    

print(f'{"Wind direction:":>30}', wind_direction)

if option == 3:
    loop == False



elif (option < 0 or option > 3):
    print('INVALID!')
    print('Enter Valid option')
    


