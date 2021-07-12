# Health management System

'''
You are a fitness trainer or a Nutrition. 
You have many clients for weight loose or muscle building or spine problem or leg problem. 
You design a diet and exercise for them.

You have 3 clients :- Harry, Rohan and Hammad.
You have to make total 6 files.

Now, you have to ask what you want to do log or retrieve?
You have to ask whose data you want to retrieve or log?

Write a function that when executed takes as input client name.
Such as a choice like :- 1 for harry, 2 for rohan and 3 for hammad.

After that if log is choosen by user, you have to ask What they want to log Diet or Exercise?
And you have to log their deit or exercise in a seperate file With the time they are doing that.
You have to store in the format :- [ Datetime  exercise/deit ]

Else if user Choose that he wants to retrieve the data, you have to ask What they want to retrieve Diet or Exercise?
You also have to create an another function to retrieve exercise or food for any client.

" def getDate():
    import datetime
    return datetime.datetime.now() "

From above Function you have to print time in file with taking input.

Atlast you have to print that you have sucessfully retrive/log(the option user choose) the data
'''

print("\t\t\t\t\t=====Welcome To Health Management System=====\n")

# Try statement so that if any error or exception occured by the user the except block will handle it.
try:
    
    # Firstly taking the choice from user to retrive or log the data as mentioned in question
    ActionsToBePerformed = int(input('''What you want to do log the data or retrive the data?
Press 1 for Log the data.
Press 2 for Retrieve the data.
Enter your Choice : '''))
    
    a = [ 1 , 2 ]

    # Applying conditional statements to check whther the entry given by the user for ActionsToBePerformed is correct or not
    if ActionsToBePerformed in a:
        pass
    else:
        print("\nInvalid choice!\n")
        exit()

    # Date Time input function
    def getDate():
        import datetime
        return datetime.datetime.now()

    # Retrieve function
    def retrieve():
        # Conditional statements for retrieveing the value of file to user according the user input
        if Type == 1:
            with open(f"{Name}_food.txt") as f:
                Data = f.read()
                print("\n" + Data)

        elif Type == 2:
            with open(f"{Name}_exercise.txt") as f:
                Data = f.read()
                print("\n" + Data)

        else:
            print("\nInvalid entry!")
            exit()

    # Log function
    def log():
        # Conditional statements for loging the value in file according the user input
        if Type == 1:
            with open(f"{Name}_food.txt", "a") as f:
                Meal = input("\nEnter the meal : ")

                # Appending the values in the food file
                f.write(f"{getDate()} {Meal}\n")

        elif Type == 2:
            with open(f"{Name}_exercise.txt", "a") as f:
                Exercise = input("\nEnter the exercise : ")
            
                # Appending the values in the exercise file
                f.write(f"{getDate()} {Exercise}\n")

        else:
            print("\nInvalid entry!")
            exit()

    # Taking name of user so that the log or retrive features can be used
    Name = input("\nEnter your name : ")

    # Taking the type in which the user need data retrieved or loged
    Type = int(input('''Please select a category!
Press 1 for Food.
Press 2 for Exercise.
Enter your Choice : '''))

    # Starting conditional statements to start the procedings with Taking ActionsToBePerformed values
    if ActionsToBePerformed == 1:
        # Calling the function which we create to log the data
        log()
        print("\nYour data has been successfully loged!\n")

    elif ActionsToBePerformed == 2:
        # Calling the function which we create to retrieve the data
        retrieve()
        print("\nYour data has been successfully retrieved!\n")
    

# Except to handle all error and exception in code while user is using it
except Exception as e:
    print("\nPlease enter valid entry!\n")

# Finally statement to thank user to use the code
finally:
    print("\nThanks for using the code!")
