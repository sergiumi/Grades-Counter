#The program manipulates a user-added list of numbers and generates output based on user requirements.
#It can print the mean, median, mode, and skewness of the list.

numberList = [] #creating an empty list to store the grades of the students inside to be able to manipulate with them in our program


# This is a function which is called mainMenu here is going to be dysplayed the menu where the user can chose to do a chenge to his own list 
# author (Sergiu Mita 22030807)
# version (version:3  date:06/05/24)
def mainMenu(): 
    while True: # I used while loop in this function to return to the main menu every time when an actitin from the menu list was succeseful done  
        print("""Hello, welcome to Students grade counter
                 - - - - - - - - - - - - - - - -
                 1. Print the Mean Number
                 2. Print the Median Number
                 3. Print the Mode Number
                 4. Print the Skewness
                 5. Add more numbers to the list
                 6. Enter a NEW set of numbers
                 7. Exit the APP
                 - - - - - - - - - - - - - - - -""") # this is a print statement that will print this string, the 3 quotation marks were used to print more than one line of this string
        
        print() # it's an empty print statement to print an empty line after the mainMenu
        chosenCategory = input("Please choose a category from Above: ") # chosenCcategory is a local variable that will store the input from the user
        print() # it's an empty print statement to print an empty line after the choosing category
                 
        if chosenCategory == "1": # an if statement is and function which allow us to make a decision,
                    # I used an if statement to allow the user to choose a category from the list which was printed above if the user  will type 1 the next print will be executed
            print('The MEAN number will be printed')
            numbers = multiNumbers()  # we are saying multi number function to the "numbers" which is a local variable to be able
                    # to manipulate with the "numberList" from the "multiNumber" function, because the "multiNumber" returning the updated list
            print(f'The MEAN number of your list {numbers} is {meanNumber(numbers)}') #in the print statement, we are printing a message for the user
                    # and printing the updated list through "numbers" variable and calling a function which is the "meanNumber" of parameter numbers,
                    # this parameter allows to call the same function but with a different input if we have multiple inputs'''
            print() # it's an empty print statement to print an empty line after to be easier to delimitate what happened
            
        elif chosenCategory == "2": # elif strands from else and if command which is used in this case as an swich mode
                   # to check the input from the user and to give the right answer when teh function was called  if the user will type 2 the next print will be executed
            print('The MEDIAN number will be printed')
            numbers = multiNumbers()
            print(f'The MEDIAN number of your sorted list {sorted(numbers)} is {medianNumber(numbers)}') #in the print statement, we are printing a message for user
                    #and printing the updateted  sorted list through "numbers" variable and calling a function which is the "medianNumber" of parameter numbers
            print()
            
        elif chosenCategory == "3": # if the user will type 3 the next print will be executed
            print('The MODE number will be printed')
            numbers = multiNumbers()
            print(f'The MODE number of your list {numbers} is {modeNumber(numbers)}') # print will show on the screen the user list and  modeNumber function answer
            print()
            
        elif chosenCategory == "4": # if the user will type 4 the next print will be executed
            print('The SKEWNESS will be printed')
            numbers = multiNumbers()
            print(f'The STANDARD DEVIATION of your list {numbers} is {standard_dev(numbers)}') # print will show on the screen the user list and standard_dev function answer
            print(f'The SKEWNESS of your list {numbers} is {Skewness(numbers)}') # print will show on the screen the user list and Skewness function answer
            print()
            
        elif chosenCategory == "5": # if the user will type 5 the program will call the multiNumbers function which will allow user to add more grades to the list
            print('You can add more numbers to the list')
            multiNumbers() #calling the multiNumbers function to add new numbers to the existing list
            print()
            
        elif chosenCategory == "6": # if the user will type 6 the program will clear the list
                    # and call the "multiNumbers" function which will allow user to insert a new roll of grades to the list
            numberList.clear()  # this inbuilt list method allow us to clear the list
            print("You can add a new set of numbers...") # printing a message to be more user friendly 
            multiNumbers()  # adding numbers to the cleared list so it looks like a new list
            print()
            
        elif chosenCategory == "7": # if the user will type 7 the program will print some messages and after will ask if you are agree to close the display window
            print("See you later")
            print("..............")
            print("Exiting the app...")
            exit() # the exit inbuilt method allows us to close the program from the terminal
            
        else:
            print("Invalid choice, please choose a valid option.") # if the user will typewill type a differnt number betwen 1 and 7 this message will be printed
            continue # the continue keyword will return bak to the main menu each time an non menu nuber was entered 


#the custom created "multiNumbers()" function allows us to insert every symbol from the keyboard and create logical instructions
#will give hints to the user to help them insert the correct symbols which are numbers in primitive types like integer and float
# author (Sergiu Mita 22030807)
# version (version:6  date:05/05/24)
def multiNumbers(): 
    while True:  # The  indefinite while loop was created to repeat the same action until the usel will insert a true value
        
         try: # The try function was implemented to catch the error witout crashing the program and to be user fridly
             
            number = input("Insert a grade and press Enter to continue or 'n' to stop: ") # the "number" local variable will store the value typed by the user
              #and colleteded by the program with the command input
            
            if number == 'n':  # if user inputs 'n', the program will exit the loop and proceed to the next statement but only if the list contains more than 2 numbers
                
                if len(numberList) < 2: # if the length of the list is less than 2 the user will be asked to insert more grades  
                    print("Please add at least two grades to the list.") # and every time the program will check its correctness because of the while loop
                    continue # this keyword allows us to go back and ask the user to insert more grades because the condition was not satisfied
                
                else: # if the condition is satisfied the program will go to the next keyword
                    break  # this give us power to stop the indefinite loop
                
            else: # if the user started to inser grades the next scenario will apply 
                number = float(number) # the numbers will be converted to float
                
                if number <= 0: # if the input number is less than 0 the user will be asked to add a positive number 
                    print("Please enter a grade bigger than '0'")
                    
                else: #if the number is bigger then 0 it will be added to the created list called numberList
                    numberList.append(number)  # an element can be added using different functions, but I chose to add, which will add it to the end of the lis
                    
         except ValueError: #the except keyword is a part of the try method which will catch the error
              # and will display a help message for the user without crashing the program
            print("Invalid input. Please type a number or 'n' to stop.") # this message will be displayed
              #if the user will type a character which is not of type int or float
            
    print()
    print("You have entered " + str(len(numberList)) + " numbers. Your list is: " + str(numberList)) # tThis print statement will display the list
              # and how many elements it contains and to be able to print it I converted the results to string type
              
    return numberList # the return keyword allows us to return the output of the changes which was made to the initial list  


# The meanNumber function is a method which calculates the average number fron the inseted list
# author (Sergiu Mita 22030807)
# version (version:1  date:06/05/24)
def meanNumber(aList): # The "meanNumber()" function accepts a list as a parameter, which needs to be specified when the function is called
    # In our case, the list is populated by the function "multiNumbers", so our parameter will be the result of calling the "multiNumbers" function
    
    meanNumber = 0 # to calculate the average number first create a variable for it and assign it to 0
    for number in aList: # looping through the list
        meanNumber += number # and adding each element of the list to that variable
        
    mean = meanNumber / len(aList) # as result the mean number is the sum of all the elements in the list divided by the length of the list 
    return mean # at the end we have to return the result


# The medianNumber() function verify the middle number of a arranged list from min to max 
# it identifies the middle number in the sorted list if the list length is odd 
# or the average of the two middle numbers if the list length is even
# author (Sergiu Mita 22030807)
# version (version:1  date:06/05/24)
def medianNumber(aList): # The "meanNumber()" function accepts a list as a parameter, which needs to be specified when the function is called
    sorted_numbers = sorted(aList) # first we create the list to sort from min to max valuewith the list method sorted
    n = len(sorted_numbers) # after calculating the length of the list with the len functoin 
    if n % 2 == 0: # if the number of elements is even, median is the average of the middle two elements
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2 # returning the output of the median number
                   #by calculating the average of the two middle numbers that we determined by their index numbers
                    
    else:# if the number of elements is odd, median is the middle element
        return sorted_numbers[n // 2] # returning the output of the median number
                   # by using floor division which will return the amount containing a number without the remainder


# Mode Number function is checking which number appears the most in the list 
# author (Sergiu Mita 22030807)
# version (version:3  date:06/05/24)
def modeNumber(aList):
    countNr = {} # create a dictionary to store the pair
    # of how many times the number belongs to the list and the number itself
    
    for num in aList: # check how many times the same number can be found in the list by looping the list 
        if num in countNr: # if the number belongs to the list 
            countNr[num] += 1 #the counter in the dictionar is growing up 
        else: # if not it is assign to 1 
            countNr[num] = 1
            
    max_count = max(countNr.values()) # find the number(s) with the highest count
    modes = []  # initialize an empty list to store the modes
    
    for num, count in countNr.items():  # iterate over key-value pairs in count_dict
        if count == max_count:  # check if the count equals the maximum count
            modes.append(num)  # if yes, add the number to the modes list
    return modes # returning the final result


# Standard_dev method calculates the standard deviation by the formula by population
# from research which will be used in the skewness calculation
# author (Sergiu Mita 22030807)
# version (version:3  date:07/05/24)
def standard_dev(aList):
   
    sumSquaredDif = 0 # Initialize a variable to store the sum of squared differences
    
    for i in aList: # Iterate through each element i in the list 
        squaredDif = (i - meanNumber(aList)) ** 2 # calculate the squared difference between the current element and the mean
        sumSquaredDif += squaredDif # add each of the squared difference to the sum of squared differences
     
    variation = sumSquaredDif / len(aList) # calculate the variation by dividing the sum of squared differences by the length of the list
    st_dev = variation ** 0.5 # calculate the standard deviation by taking the square root of the variation which is the same as 1**0.05
    return st_dev # return the calculated standard deviation



# Skewness function calculates the asymmetry of the grades in the list by using a formula
# author (Sergiu Mita 22030807)
# version (version:1  date:07/05/24)
def Skewness(aList): # a new procedure with a parameter
    Skew = 3*(meanNumber(aList)- medianNumber(aList))/ standard_dev(aList) # creating a local variable
        # skew and assigning a formula that calculates skewness
    return  Skew # returning the result of the asymmetry in the list


mainMenu() #calling the main method to start the program



