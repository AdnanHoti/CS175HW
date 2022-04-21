import random

li=[]
for i in range(10):
    li.append(random.randint(1,100))

print("Elements in list are: ",li,"\n")

print(f"First,fifth and last element in the list:{li[0]} {li[4]} {li[-1]}\n")
print("Every element at even index: ")
for i in range(10):
    if i%2==0:
        print(li[i],end=' ')
        
print("\nEvery even element: ")
for i in li:
    if i%2==0:
        print(i,end=' ')

print("\nEvery odd element: ")
for i in li:
    if i%2==1:
        print(i,end=' ')
        
min_else=min(li)
print(f"\nMinimum element in the list is {min_else} and index(es) of minimum element: ")
for i in range(10):
    if li[i]==min_else:
        print(i,end=' ')
        
max_else=max(li)
print(f"\nMaximum element in the list is {max_else} and index(es) of maximum element: ")
for i in range(10):
    if li[i]==max_else:
        print(i,end=' ')

sum=0       
for i in li:
    sum+=i
avg=sum/10

greaterElementCount = 0
for i in li:
    if i > avg:
        greaterElementCount += 1
print(greaterElementCount)

alternate_sum=0
for i in range(10):
    if i%2==0:
        alternate_sum+=li[i]
    else:
        alternate_sum-=li[i]
print(f"\nAlternate sum: {alternate_sum}")

li.reverse()
print("\nElements in reverse order: ",li)
li.sort(reverse=True)
print("\nElements in sorted order: ",li)
