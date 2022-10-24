
customerNames = ['Jane Cloud', 'Andy Spice', 'Hello There', 'Safe Secure']
customerPins = ['1234', '5678', '9012', '3456']
customerBalances = [1000000, 300000, 150000, 600000]

deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

# The statement below helps the program to run continuously.
while True:

#THE HOME PAGE
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("         Welcome to My Bank           ")
    print("              HOME PAGE                ")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
    print("**<< 1. Open a new account         >>**")
    print("**<< 2. Withdraw Money             >>**")
    print("**<< 3. Deposit Money              >>**")
    print("**<< 4. Check Customers & Balances >>**")
    print("**<< 5. Exit                       >>**")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")



    choiceNumber = input("Select Your Number Of Choise from the Home Page : ")


#THE CODE FOR OPENING A NEW ACCOUNT
#(Choice 1)
    if choiceNumber == "1":
        print("===============================")
        print("     OPENING A NEW ACCOUNT     ")
        print("===============================")

# The line below will take the no:of customers from the user.
        NOC = eval(input("Number of Customers : "))
        i = i + NOC

# The if condition will restrict the number of new account to 100.
        if i > 100:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - NOC
        else:

# The while loop will run according to the no:of customers.
            while counter_1 <= i:

# These few lines will take information from customer and then append them to the list.
                name = input("Please Enter Your Full Name : ")
                customerNames.append(name)

                pin = str(input("Please Enter Password Of Your Choice : "))
                customerPins.append(pin)

                balance = 0
                deposition = eval(input("Please Deposit Some Money To Start An Account : "))
                balance = balance + deposition
                customerBalances.append(balance)

                print("\nName=", end=" ")
                print(customerNames[counter_2])

                print("Password=", end=" ")
                print(customerPins[counter_2])

                print("Balance=", end=" ")
                print(customerBalances[counter_2], end=" ")

                print("-/Ksh")

                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1

                print("\n----New Account Created Successfully !----")

                print("\n")

                print("Your Name is Now Available On The Customers List : ")
                print(customerNames)

                print("\n")

                print("Note! Please Remember Your Name and Password")
                print("========================================")
                break


# The statement below helps the user to go back to Home Page.
        mainMenu = input("Choose Option 0 to go Back to the Home Page ...")


# THE CODE FOR WITHDRAWING MONEY
#(Choise 2)
    elif choiceNumber == "2":
        print("===============================")
        print("         WITHDRAW MONEY        ")
        print("===============================")

        j = 0

# The while loop will prevent the user using the account if the username or pin is wrong.
        while j < 1:
            k = -1

            name = input("Please Enter Your Name : ")
            pin = input("Please Enter Your Password : ")

# This while loop will keep the function running when variable k is smaller than length of the
            while k < len(customerNames) - 1:
                k = k + 1

 # These two if conditions find where both the Name and Password matches.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1

# These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Ksh\n")
                        balance = (customerBalances[k])

# Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input("Enter Amount You Wish To Withdraw : "))

# The if condition below would look whether the withdraw is greater than the balance.
                        if withdrawal > balance:

# This statement below would take a deposition from the customer.
                            deposition = eval(input(
                                "Please Deposit a higher Amount because your Balance mentioned above is not enough : "))

# These few statements would update the Amount and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Ksh\n")

                            balance = balance - withdrawal
                            print("-\n")
                            print("Confirm you have successfully withdraw ", withdrawal, end=" ")
                            print("-/Ksh\n\n")

                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Ksh\n\n")
                        else:

# Else condition mentioned above is to do withdrawal if the balance is greater than the withdraw amount.
                            balance = balance - withdrawal

# These few statement would update the values in the list and show it to the customer.
                            print("\n")
                            print("Confirmed you have successfully withdraw ", withdrawal, end=" ")
                            print("-/Ksh")

                            customerBalances[k] = balance
                            print("Your New Balance Is: ", balance, end=" ")
                            print("-/Ksh\n\n")
            if j < 1:

# The if condition above would work when the Password or the Name is wrong. Ke
                print("Your Name and Password does not match!\n")
                break

# The statement below helps the user to go back to the Home Page(main menu).
        mainMenu = input("Choose Option 0 to go Back to the Home Page ...")


#CODE FOR DEPOSITING MONEY TO THE ACCOUNT
#(Choise 3)
    elif choiceNumber == "3":
        print("===============================")
        print("         DEPOSIT MONEY         ")
        print("===============================")

        n = 0

# The while loop below would work when the password or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please Enter Your Name : ")
            pin = input("Please Enter Your Password : ")

# The while loop below will keep the function running to find the correct user.
            while k < len(customerNames) - 1:
                k = k + 1

# The two if conditions below would find whether both the pin and the name is correct.
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1

#The statements below would show the customer balance and update list values according to the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Ksh")
                        balance = (customerBalances[k])

#The statement below takes the deposition from the customer.
                        deposition = eval(input("Enter The Amount You Want To Deposit : "))
                        balance = balance + deposition
                        customerBalances[k] = balance

                        print("\n")
                        print("Confirmed You Have Successfully Deposit Is ", deposition, end=" ")
                        print("-/Ksh")

                        print("Your New Balance: ", balance, end=" ")
                        print("-/Ksh\n\n")
            if n < 1:
                print("Your Name And Password Does Not Match!\n")
                break

#The statement below helps the user to go back to the Home Page.
        mainMenu = input("Choose Option 0 to go Back to the Home Page ...")


#THE CODE FOR CHECKING CUSTOMERS AND THEIR BALANCE
#(Choice 4)
    elif choiceNumber == "4":

        print("===============================")
        print("    CHECKING CUSTOMERS LIST    ")
        print("===============================")

        k = 0
        print("Customers Name list and balances mentioned below : ")
        print("\n")

# The while loop below will keeping running until all the customers and balances are shown.
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("sKsh")
            print("\n")
            k = k + 1
#The statement below helps the user to go back to the Home Page.
        mainMenu = input("Choose Option 0 to go Back to the Home Page ...")


#THE CODE FOR EXIT
#(Choice 5)
    elif choiceNumber == "5":
        print("===============================")
        print("         YOU HAVE EXIT         ")
        print("===============================")

#These statements would be just showed to the customer.
        print("Thank you for using IAT Bank!")
        print("Come Again For Best Banking Services")
        print("Bye Bye")
        break
    else:

# This else function above would work when a wrong Kelvin Did it function is chosen.
        print("Invalid option")
        print("Please Try again!")

# The statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Choose Option 0 to go Back to the Home Page ...")