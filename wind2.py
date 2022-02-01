#Adnan Hoti 
temp_fah = 34.6
temp_cel = 1.4
wind_speed = 23
wind_direction = 'North'
station_name = 'Monmouth University'
print('Weather Station Name:', station_name)
temp_fah = float(input('What is the current tempature(Fahrenheit)?:'))
wind_speed = int(input('What is the wind speed?:'))
wind_direction = print('What is the wind direction?:', wind_direction)

print()
print('Monmouth University Weather Station')
print()
print('Tempature(Fahrenheit):', f'{temp_fah:,.1f}')
print('Tempature(Celcius):', f'{temp_cel:,.1f}')
print('Wind(mph):', wind_speed)
print('Wind direction:', 'North')
