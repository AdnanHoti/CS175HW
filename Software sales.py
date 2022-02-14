#Adnan Hoti
#Software Sales

retail_Amount = 99
packages = int(input('Enter the quantity of retail packages: '))
Tot_Amount = packages * retail_Amount
discount_0 = 0
Discount_1 = 0.1
Discount_2 = 0.2
Discount_3 = 0.3
Discount_4 = 0.4
if packages <= 1 and packages <= 9:
    TotalAmountPurchased_0 = Tot_Amount - Tot_Amount * Discount_0
    print('Amount of discount is:')
    print('Total amount of purchase after discount:')
if packages >= 10 and packages <=19:
    TotalAmountPurchased_1 = Tot_Amount - Tot_Amount * Discount_1
    print(' Amount of discount is: ',Tot_Amount * Discount_1)
    print('Total amount of purchase after discount: ', TotalAmountPurchased_1)

elif packages >= 20 and packages <= 49:
    print(' Amount of discount is: ',Tot_Amount * Discount_2)
    TotalAmountPurchased_2 = Tot_Amount - Tot_Amount * Discount_2
    print('Total amount of purchase after discount: ' ,TotalAmountPurchased_2 )
elif packages >= 50 and packages <= 99:
    print('Amount of discount is: ',Tot_Amount * Discount_3)
    TotalAmountPurchased_3 = Tot_Amount - Tot_Amount * Discount_3
    print('Total amount of purchase after discount: ' ,TotalAmountPurchased_3)
else:
    if packages >=100:
        print('Amount of discount is: ',Tot_Amount * Discount_4)
        TotalAmountPurchased_4 = Tot_Amount - Tot_Amount * Discount_4
        print('Total amount of purchase after discount: ' ,TotalAmountPurchased_4)
