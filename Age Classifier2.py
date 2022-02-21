#Adnan Hoti
#Age Classifier



Age = float(input("Enter person's age: "))


if (Age > -1 and Age <= 1 ) :

    print ("Person is an infant.")

elif (Age > 1 and Age < 13 ) :

    print ("Person is a child.")

elif ( Age >= 13 and Age < 20 ) :

    print ("Person is a teenager.")

elif(Age >= 20):

    print ("Person is an adult.")


elif (Age < 0 and Age > 150):
    print('INVALID!')
    



    
