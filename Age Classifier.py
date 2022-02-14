#Adnan Hoti
#Age Classifier

age = int(input('Please enter a persons age:'))

if age <= 1:
    print('The person is an infant')
else:
    print('The person is not an infant')

if age > 1 and age > 13:
    print('The person is a child')
else:
    print ('The person is not an infant')

if age <= 13 and age > 20:
    print('The person is a teenager')
else:
    print ('The person is not a teenager')

if age >=20:
    print ('The person is an adult')

if age > 150:
    print('Error!')

if age < 0:
    print('Error!')


    
