def currencyConverter():

    

    currency = {"United States Dollar" : 1,
                "Japanese Yen" : 148.19,
                "European Union Euro" : 1.01,
                "British Pound-Sterling" : 0.87,
                "Chinese Yuan" : 7.28}

    trans = input("Please enter which type of currency you currently have. Choose from the list:\n" + '1.' + "United States Dollar\n" + '2.' + "Japanese Yen\n" + '3.' + "European Union Euro\n" + '4.' + "British Pound-Sterling\n" + '5.' + "Chinese Yuan\n")
    trans = int(trans)

    trans2 = input('How much money do you have?\n')
    trans2 = int(trans2)
    
    trans3 = input('What currency do you want to convert it to? Choose from the list:\n' + '1.' + "United States Dollar\n" + '2.' + "Japanese Yen\n" + '3.' + "European Union Euro\n" + '4.' + "British Pound-Sterling\n" + '5.' + "Chinese Yuan\n")
    trans3 = int(trans3)               


    if (trans == 1) and (trans3 == 1):

        x = currency.get("United States Dollar") * trans2
        print("You have..." + str(x) + " Dollars")
    
    if (trans == 1) and (trans3 == 2):

        x = currency.get("United States Dollar") * trans2 * currency.get("Japanese Yen")
        print("You have..." + str(x) + " Yen")

    if (trans == 1) and (trans3 == 3):

        x = currency.get("United States Dollar") * trans2 * currency.get("European Union Euro")
        print("You have..." + str(x) + " Euros")

    if (trans == 1) and (trans3 == 4):

        x = currency.get("United States Dollar") * trans2 * currency.get("British Pound-Sterling")
        print("You have..." + str(x) + " Pounds") 
        
    if (trans == 1) and (trans3 == 2):

        x = currency.get("United States Dollar") * trans2 * currency.get("Chinese Yuan")
        print("You have..." + str(x) + " Yuan")

        


    if (trans == 2) and (trans3 == 1):

        x = currency.get("Japanese Yen") * trans2 * currency.get("United States Dollar")
        print("You have..." + str(x) + " Dollars")
    
    if (trans == 2) and (trans3 == 2):

        x = currency.get("Japanese Yen") * trans2 
        print("You have..." + str(x) + " Yen")

    if (trans == 2) and (trans3 == 3):

        x = currency.get("Japanese Yen") * trans2 * currency.get("European Union Euro")
        print("You have..." + str(x) + " Euros")

    if (trans == 2) and (trans3 == 4):

        x = currency.get("Japanese Yen") * trans2 * currency.get("British Pound-Sterling")
        print("You have..." + str(x) + " Pounds") 
        
    if (trans == 2) and (trans3 == 2):

        x = currency.get("Japanese Yen") * trans2 * currency.get("Chinese Yuan")
        print("You have..." + str(x) + " Yuan")




    if (trans == 3) and (trans3 == 1):

        x = currency.get("European Union Euro") * trans2 * currency.get("United States Dollar")
        print("You have..." + str(x) + " Dollars")
    
    if (trans == 3) and (trans3 == 2):

        x = currency.get("European Union Euro") * trans2 * currency.get("Japanese Yen")
        print("You have..." + str(x) + " Yen")

    if (trans == 3) and (trans3 == 3):

        x = currency.get("European Union Euro") * trans2
        print("You have..." + str(x) + " Euros")

    if (trans == 3) and (trans3 == 4):

        x = currency.get("European Union Euro") * trans2 * currency.get("British Pound-Sterling")
        print("You have..." + str(x) + " Pounds") 
        
    if (trans == 3) and (trans3 == 2):

        x = currency.get("European Union Euro") * trans2 * currency.get("Chinese Yuan")
        print("You have..." + str(x) + " Yuan")



    if (trans == 4) and (trans3 == 1):

        x = currency.get("British Pound-Sterling") * trans2 * currency.get("United States Dollar")
        print("You have..." + str(x) + " Dollars")
    
    if (trans == 4) and (trans3 == 2):

        x = currency.get("British Pound-Sterling") * trans2 * currency.get("Japanese Yen")
        print("You have..." + str(x) + " Yen")

    if (trans == 4) and (trans3 == 3):

        x = currency.get("British Pound-Sterling") * trans2 * currency.get("European Union Euro")
        print("You have..." + str(x) + " Euros")

    if (trans == 4) and (trans3 == 4):

        x = currency.get("British Pound-Sterling") * trans2 
        print("You have..." + str(x) + " Pounds") 
        
    if (trans == 4) and (trans3 == 5):

        x = currency.get("British Pound-Sterling") * trans2 * currency.get("Chinese Yuan")
        print("You have..." + str(x) + " Yuan")






    if (trans == 5) and (trans3 == 1):

        x = currency.get("Chinese Yuan") * trans2 * currency.get("United States Dollar")
        print("You have..." + str(x) + " Dollars")
    
    if (trans == 5) and (trans3 == 2):

        x = currency.get("Chinese Yuan") * trans2 * currency.get("Japanese Yen")
        print("You have..." + str(x) + " Yen")

    if (trans == 5) and (trans3 == 3):

        x = currency.get("Chinese Yuan") * trans2 * currency.get("European Union Euro")
        print("You have..." + str(x) + " Euros")

    if (trans == 5) and (trans3 == 4):

        x = currency.get("Chinese Yuan") * trans2 * currency.get("British Pound-Sterling")
        print("You have..." + str(x) + " Pounds") 
        
    if (trans == 5) and (trans3 == 2):

        x = currency.get("Chinese Yuan") * trans2 
        print("You have..." + str(x) + " Yuan")




def 


def main():

    currencyConverter()



if __name__ == "__main__":

    main()
    
    
    
    
    def main():
    
    fruits = ["apple"," orange", "banana", "begel", "cabbage", "spinach", "milk", "eggs", "cake", "pasta"]
    
    #dictionaries are defined as a set of key : value' pairs
    
    fruits2 = {"apple" : 1.50,
                "orange" : 1.00,
                "banana" : 1.25,
                "bagel" :1.25,
                "cabage" : 1.50,
                "spinach" :4.25,
                "milk" : 2.75,
                "eggs" : 3.25,
                "cake" : 8.00,
                "pasta": 3.50}
                
                
    print(fruits2)

if __name__ == "__main__":
     main()
