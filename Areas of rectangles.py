#Adnan Hoti
#Areas of Rectangles


length_1 = float(input('Enter length for triangle 1:'))
width_1 = float(input('Enter width for triangle 1:'))

area_1 = length_1 * width_1

length_2 = float(input('Enter length for triangle 2:'))
width_2 = float(input('Enter width for triangle 2:'))

area_2 = length_2 * width_2

if area_1 > area_2:
    print('Rectangle 1 is greater!')
elif area_2 > area_1:
    print('Rectangle 2 is greater!')
elif area_1 == area_2:
    print('Rectangles 1 and 2 are the same!')
