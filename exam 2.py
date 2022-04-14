#Adnan Hoti

def main():
    get_month = []

    for count in range(12):
        get_temperature = float(input('Enter a temperature for the month: '))
        get_month.append(get_temperature)

    print('Temperature entered:', get_month)

    lowest_temp = min(get_month)
    print('Lowest temperature:', lowest_temp)

    highest_temp = max(get_month)
    print('Highest temperature:', highest_temp)

    average_temperature = sum(get_month) / 12
    print('Average temperature: {:.1f}'.format(average_temperature))

    for i in get_month:
          if i > average_temperature:
              count = count + 1
    count_months = print("The numbers greater than the average : " + str(count))
    
   
main()

