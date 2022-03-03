n = int(input('Please enter integer:'))

def getSortedNumber(n):
  
    
    number = str(n)
     
    number = ''.join(sorted(number))
     
    number = int(number)
   
    return number
   
print(getSortedNumber(n))

count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)


sum = n

for i in range (n):
    if (i % 2 == 0):
        sum += i
print('The sum of even digits:',sum)
