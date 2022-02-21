#Question 1 part a:

n = float(input("Please enter a positive number: "))

square = 0.0

while square < n:
    square = square + 1
    print(square * square)


#part b:

n = int(input("Enter a number n: "))
divisible_10 = []
for i in range(0, n):
    if i % 10 == 0:
        divisible_10.append(i)

print(divisible_10)

#Part c

number = int(input("Enter a number: "))
exponent = 0

while exponent <= number:
    result = 2 ** exponent  
    exponent = exponent + 1
    print(result)

 
#Part d:
    n = 2
x = int(input("What is your input?:"))

while x < x+1:
  n = n ** x
  exponent = x
  + 1
  print (n)

#part e

N = int(input("enter the last number "))
sum = 0 
for i in range(0,n+1):
    if(i%2!=0):

        sum=sum + i 
Print(sum) 


#Question 2

for i in range(10, 31, 5):
    print ('After ',i,' minutes, you burned ', i*4.2)

#Question 3

def main():
    """
Python program that calculates distance
    """

speed = int(input("\n Enter the speed of the vehicle in mph:"));
hours = int(input("\n\n Enter the number of hours travelled:"));
hour = 1;
print("\n\n%-10s%-10s\n"%("Hours","Distance"));
print("\n________________________");
while hour <= hours:
    distance = speed * hour;
print("\n%-10d%-10d" %(hour, distance));
hour +=1;
print("\n\n");
main();

#question 4
n = int(input("Enter a nonnegative integer:"))
while n<0:
     n = int(input("Enter a nonnegative integer:"))
fact = 1
for i in range(1,n+1):
     fact = fact * i
print(fact)

