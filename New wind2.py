temp_valid = True
windspeed_valid = True
temp_fah = 34.6
temp_cel = (5/9) * (temp_fah-32)
wind_speed = 23

station_name =input('What is the Weather Station Name?:')
print('Welcome to', station_name, 'Weather Station')
is_Running = True
is_Option1Selected = False
while is_Running:
    print('Option 1: Input')
    print('Option 2: Print')
    print('Option 3: Exit')
    Choice = input("Enter your option:")
    if Choice=='1':
        temp_fah = float(input('What is the current tempature(Fahrenheit)?:'))
        while temp_fah < -130 or temp_fah > 150:
            print('Invalid input!')
            temp_fah=float(input('What is the current temp(fah)?'))
        wind_speed=int(input('What is the wind speed(mph)?'))
        while wind_speed<0:
            print('The wind speed is invalid')
            wind_speed=int(input('What is the wind speed(mph)?'))
        wind_direction=input('what is the wind direction?')
        is_Option1Selected=True
    elif Choice == '2':
        if is_Option1Selected:
            print( )
            str_temp_fah='Tempature(Fahrenheit):'
            str_temp_cel='Temperatur(Celcius):'
            str_wind_speed='Wind Speed(mph):'
            str_wind_direction='What is the wind direction?:'
            temp_cel=(temp_fah-32)/1.8
            print(f'{"Tempature(Fahrenheit):":>30}', f'{temp_fah:,.1f}')
            print(f'{"Tempature(Celcius):":>30}', f'{temp_cel:,.1f}')
            print(f'{"Wind Speed(mph):":>30}', wind_speed)
            print(f'{"Wind direction:":>30}', wind_direction)
        else:
            print('No data to select, pick option 1 to start')
    elif Choice == '3':
        print('Goodbye!')
        is_Running=False
    else:
        print('The choice is invalid')
        

        
