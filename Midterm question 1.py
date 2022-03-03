month = input("Enter a month: ")
season = ''

if month == 1 or month == 2 or month == 3:
    season = 'Winter'

elif month == 4 or month == 5 or month == 6:
    season = 'Spring'

elif month == 7 or month == 8 or month == 9:
    season = 'Summer'

elif month == 10 or month == 11 or month == 12:
    season = 'Fall'
    
print('It is', season)

