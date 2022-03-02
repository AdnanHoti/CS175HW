#Question 1 part a:

num = int(input('Enter a number:'))
x = 0
a= 0
y= []
while(a<num):
    a = x*x
    if a!=num and a<num:
        y.append(a)
        x+=1
print(*y)


#part b:

n = int(input("Enter a number n: "))
divisible_10 = []
for i in range(10, n):
    if i % 10 == 0:
        divisible_10.append(i)

print(divisible_10)

#Part c

number = int(input("Enter a number: "))
num = 1
for i in range(n):
    if(num<n):
        print(num,end=" ")
    num*=2
print("\n")

 
#Part d:
from itertools import count
for x in (2**y for y in count(1)):
    if x > 64:
        break
    print(x)

#part e
num = int(input(" Please Enter N: "))
 
for number in range(1, num + 1):
    if(number % 2 != 0):
        print("{0}".format(number))

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

