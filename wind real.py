temp_fah = 34.6
temp_cel = (5/9) * (temp_fah-32)
wind_speed = 23
station_name =input('What is the Weather Station Name?:')
temp_fah = float(input('What is the current tempature(Fahrenheit)?:'))
wind_speed = int(input('What is the wind speed?:'))
wind_direction = input('What is wind direction?:')
print()
print('\t'+station_name+' Weather Station')
print()
print(f'{"Tempature(Fahrenheit):":>30}', f'{temp_fah:,.1f}')
print(f'{"Tempature(Celcius):":>30}', f'{temp_cel:,.1f}')
print(f'{"Wind Speed(mph):":>30}', wind_speed)
print(f'{"Wind direction:":>30}', wind_direction)
