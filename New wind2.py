temp_valid = True
windspeed_valid = True
temp_fah = 34.6
temp_cel = (5/9) * (temp_fah-32)
wind_speed = 23
station_name =input('What is the Weather Station Name?:')

message = input('\n Input weather reading? (y/Y for yes, n/N for no):')
if message.lower() == 'no':
    print('Goodbye!')

elif message.lower() == 'yes':
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

message = input('\n Output the weather reading? (y/Y for yes, n/N for no):')
if message.lower() == 'no':
    print('Goodbye!')

elif message.lower() == 'yes':
    print('\t'+station_name+' Weather Station')

if temp_valid == True:
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
