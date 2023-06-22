#Program allowing user access to two financial calculators:
#investment calculator and a home loan calculator

import math


#Function to validate the user input for a string
def user_input_string_validation(input_request, option_1, option_2):
    #Create a boolean to break the loop after validation
    string_validated = False
    #Create a list with the two options, to validate the user input against
    string_options = [option_1, option_2]

    #Create the loop to validate the input
    while not string_validated:
        #Add .title() to ensure variable selection is homogenous
        user_string_input = input(input_request).title()

        if user_string_input in string_options:
            string_validated = True
        else:
            print("You've entered an invalid option, please try again\n")

    return user_string_input


#Function to validate the user input for an integer
def user_input_int_validation(input_request):
    #Create a boolean to break the loop after validation
    int_validated = False

    #Create the loop to validate the input
    while not int_validated:
        try:
            user_num_input = int(input(input_request))
            int_validated = True
        except ValueError as error1:
            print(error1)
            print("Invalid input. Please try again\n")

    return user_num_input 


#Introducing the options to the user
print("\nInvestment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan \n")

selection = user_input_string_validation("Enter either 'Investment' or 'Bond' from the menu above to proceed: ", "Investment" , "Bond")

if (selection == "Investment"): #Condition 1: Investment calculator has been chosen

    #The following values cannot be stored as strings, as they are needed for 
    #further calculation
    #Float is used for the amount because monetary values can go to 2 decimal places
    while True:
        try:
            initial_deposit_amount = float(input("How much are you depositing initially? £"))
            break
        except ValueError as error1:
            print(error1)
            print("Invalid input. Please try again\n")

    interest_rate = user_input_int_validation("What is the interest rate(Whole number): ")/100
    number_years_investing = user_input_int_validation("How many years are you investing? ")

    #Validating the user input for interest type
    interest_type = user_input_string_validation("\nDo you want to calculate 'simple' or 'compound' interest?: ", "Simple", "Compound")

    if (interest_type == "Simple"): #Condition 1: Calculating value with simple interest

        value_after_interest = initial_deposit_amount *(1 + (interest_rate * number_years_investing))
        #Rounding the value to 2 decimal points:https://www.geeksforgeeks.org/how-to-round-numbers-in-python/
        value_after_interest = round(value_after_interest, 2)
        print(f"\nValue after interest: \t£{value_after_interest}")
        
    else: #Condition 2: Calculating value with compound interest
        
        #Calculating the value after compound interest
        value_after_interest = initial_deposit_amount * math.pow((1 + interest_rate), number_years_investing)
        value_after_interest = round(value_after_interest, 2)
        print(f"\nValue after interest: \t£{value_after_interest}")
    
else: #Condition 2: Bond calculator has been chosen
    
    while True:
        try:
            present_house_value = (float(input("Please input the present value of your house: £")), 2)
            break
        except ValueError as error2:
            print(error2)
            print("Invalid input. Please try again\n")

    annual_interest_rate = user_input_int_validation("What is the yearly interest rate: ")/100
    number_months_for_repayment = user_input_int_validation("Over how many months do you plan to repay the bond? ")

    #Calculating the monthly interest rate requires dividing by 12
    monthly_interest_rate = annual_interest_rate / 12
    #Calculate monthly repayments
    monthly_repayment_value = (monthly_interest_rate * present_house_value)/(1- (1 + monthly_interest_rate)**(-number_months_for_repayment))
    monthly_repayment_value = round(monthly_repayment_value, 2)
    print(f"\nMonthly repayment value: \t£{monthly_repayment_value}")
    

