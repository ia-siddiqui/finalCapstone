#Program that allows the viewing, addition and editing of tasks + users within a company after logging in.
#This program uses lists and dictionaries for the main functionality, with the data being stored in text files

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"


#================================General program functions==============================
#Generate user file if it doesn't exist
def generate_user_file():

    # If no user.txt file or it's empty, write one with a default account
    #https://pythonhow.com/how/check-if-a-text-file-is-empty/ 
    if (not os.path.exists("user.txt")) or (os.path.getsize("user.txt") == 0):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")


#To create tasks, task_overview and user_overview text files 
def generate_empty_txt_file(file_name):
    
    if not os.path.exists(file_name):
        with open(file_name, "w") as default_file:
            #Pass used when you want empty code without throwing an error
            #https://www.simplilearn.com/tutorials/python-tutorial/pass-in-python 
            pass
    
   
#Function reading tasks.txt to create the tasks list, with a dictionary for each task
def generate_task_list():
    #reading from the tasks file, creating a list with each line as a string, then eliminating empty strings
    with open("tasks.txt", 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    #Looping through the list with each line, adding the line components to a dictionary, then adding each
    #task dictionary to a list
    t_list = []
    for t_str in task_data:
        curr_t = {}

        # Split by semicolon and manually add each component
        task_components = t_str.split(";")
        curr_t['username'] = task_components[0]
        curr_t['title'] = task_components[1]
        curr_t['description'] = task_components[2]
        curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        curr_t['completed'] = task_components[5] 

        t_list.append(curr_t)

    return t_list


#This code reads usernames and password from the user.txt file and writes it to a dictionary
def create_username_password_dict():
    #reading from the user file, creating a list with each line as a string
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")

    # Splitting each string in the list into the key and value of a dictionary with users + passwords
    user_pass = {}
    for user in user_data:
        username, password = user.split(';')
        user_pass[username] = password

    return user_pass


#We have a few places where we want string user inputs, so a validation function is created
def user_input_string_validation(request, option1, option2):
    #Variables created for validation 
    choice_validated = False
    choices = [option1,option2]
    print(request)

    #Loops around until the user selects option1 or option2
    while not choice_validated:
        user_input_choice = input(f"Choose from the options, {option1} or {option2}: ").capitalize()
        #If the input is either of the options, the loop break condition is satisfied
        if user_input_choice in choices:
            choice_validated = True
        else:
            print("\nInvalid choice. Please try again.\n")

    return user_input_choice


#Function overwriting the tasks txt to add new tasks or amend old data-applied in add_task() and view_mine()
def overwriting_task_txt():
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                t['completed'] 
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


#Function for printing the tasks - applied in add_task, view_all and view_mine
def print_task(list):
    display_str = "--------------------------------------------------------------------------\n"
    display_str += f"Task: \t\t\t {list[0]}\n"
    display_str += f"Assigned to: \t\t {list[1]}\n"
    display_str += f"Date Assigned: \t\t {list[2].strftime(DATETIME_STRING_FORMAT)}\n"
    display_str += f"Due Date: \t\t {list[3].strftime(DATETIME_STRING_FORMAT)}\n"
    display_str += f"Task Complete? \t\t {list[4]}\n"
    display_str += f"Task Description: \n {list[5]}\n"
    display_str += "--------------------------------------------------------------------------\n"
    print(display_str)


#Task due date time validation - applied in add_task and view_mine(for editing the date)
def task_due_date_validation():
    date_validated = False
    present_date = datetime.now()
    
    while not date_validated:
        try:
            task_due_date = input("\nDue date of task (YYYY-MM-DD): ")
            due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
        except ValueError:
            print("\nInvalid datetime format. Please use the format specified\n")
        
        #Ensuring the due date is not before the current date
        if due_date < present_date:
            print("\nThe date entered is before the present date. Please try again")
        else:
            date_validated = True   
            print("\n")

    return due_date

#=========================================Logging in========================================================
#Create a login function, to ensure a non-employee cannot access any of the employee data using a while loop.
def login():
    #Variables created for validation and to ensure user isn't stuck in a loop
    logged_in = False
    loop_num = 0
    while not logged_in:
        '''
        After the user has been asked once for the login details, they might not know any other users or 
        the correct password. To ensure they're not stuck in a loop, they're asked if they want to try again,
        else they won't login, but they will exit the loop and the program.
        '''
        if loop_num > 0:
            #Asking if they wish to continue and validating the answer
            try_again_request = user_input_string_validation("Do you wish to try again? If you don't login, you will be unable to access the rest of the program features.", "Y", "N")
            if try_again_request == "N":
                print("\nSorry, you have not logged in and so are unable to access the rest of the program features. The program will end here for \nyou. Goodbye\n")
                break

        print("\nLOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        #Checking if user exists or not
        if curr_user not in username_password.keys():
            print("User does not exist. \n")
        #Checking if password matches
        elif username_password[curr_user] != curr_pass:
            print("Wrong password.\n")
        else:
            print("\nLogin Successful!\n")
            logged_in = True
        
        #add to variable to keep track of loop number
        loop_num += 1
    
    return logged_in, curr_user



#==========================================Menu options======================================
#function to present the options,  and validate user input for the menu selection
def menu_options():
    #Variables created for validation 
    choice_validated = False
    choices = ['r','a','va','vm','gr','ds','cu','e']

    #Loops around until the user selects one of the options
    #Change user option added as some options are admin only
    while not choice_validated:
        menu_input = input('''Select one of the following Options below:
        r - Registering a user (admin only)
        a - Adding a task
        va - View all tasks
        vm - View my task
        gr - generate reports (admin only)
        ds - Display statistics (admin only)
        cu - change user
        e - Exit
        : ''').lower() #making sure that the user input is converted to lower case

        #If the input is one of the options, the loop break condition is satisfied
        if menu_input in choices:
            print("")
            choice_validated = True
        else:
            print("\nInvalid option entered. Please try again\n")

    return menu_input



#====================================Registering the user==============================================
#function to register a new user. If user and password are validated, the new username_password dictionary 
#overwrites user.txt 
def reg_user():
    #Variable created for validation 
    new_user_added = False

    #Loops around until a new user with matching password attempts or the user no longer wishes to try
    while not new_user_added:
        new_username = input("\nNew Username: ")
        # - Request input of a new password
        new_password = input("New Password: ")
        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the user exists already.
        if new_username in username_password.keys(): #Condition 1: the user already exists
            print("\nThis user already exists.\n")
            #Ask the user if they want to try again
            try_again_request = user_input_string_validation("Do you wish to try again? You will return to the options menu otherwise", "Y", "N")
            if try_again_request == "N": #if they don't wish to continue, the loop will break and the user sent back to the options menu
                break
        else: #Condition 2: The user does NOT already exist
            if new_password == confirm_password: #Condition I: passwords match
                # - If they are the same, add them to the user.txt file,
                print("\nNew user added\n")
                #Add the new user to the username_password dictionary
                username_password[new_username] = new_password
                '''
                Overwriting the text file to include the new addition. We loop through
                the username_password dictionary, as it has the new user added. Then we
                format each username + password for the text file and append it to a list. 
                That list is then 
                '''    
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))

                #Changing the boolean to break the while loop
                new_user_added = True
            else: #Condition II: passwords don't match
                print("\nPasswords do no match. Please try again\n")



#=======================================Adding a task=============================================
#Function adds tasks. After valdiating input, the updated task_list overwrites tasks.txt
def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and 
        - the due date of the task.'''
    task_username_validated = False
    #validating the username input
    while not task_username_validated:
        task_username = input("\nName of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        else:
            task_username_validated = True
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    #Date input
    due_date_time = task_due_date_validation()
    
    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
                "username": task_username,
                "title": task_title,
                "description": task_description,
                "due_date": due_date_time,
                "assigned_date": curr_date,
                "completed": "No"
            }
    
    #Printing the new task to the terminal
    print("\nNew task\n")
    #creating a list containing elements for print_task function
    new_task_print_list = [task_title,task_username,curr_date,due_date_time,"No",task_description]
    print_task(new_task_print_list)

    task_list.append(new_task)
    overwriting_task_txt()
    print("\nTask successfully added.\n\n")



#================================Viewing all the tasks====================================
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
       format of Output 2 presented in the task pdf (i.e. includes spacing
       and labelling) 
            '''
    # task_list = generate_task_list()

    loop_number = 1
    for t in task_list:
        print(f"\nTask {loop_number}")
        #creating a list containing elements for print_task function
        view_all_print_list = [t['title'],t['username'],t['assigned_date'],t['due_date'],t['completed'],t['description']]
        print_task(view_all_print_list)

        loop_number += 1
        


#================================View Mine functions =========================================
#Function for viewing the current user's tasks, with the option to edit a task
def view_mine(cur_user):
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    #Printing the user specific tasks and creating a list
    user_specific_task_list = print_user_specific_tasks_and_produce_list()

    if len(user_specific_task_list) == 0:
        print(f"{cur_user} has no tasks\n")
    else:
        #Asking the user what task they want to edit
        user_task_edit_index, edit_request = user_task_selection(user_specific_task_list)

        #Now user chooses whether to mark as complete or edit the task
        if edit_request:
            edit_user_specific_task(user_specific_task_list, user_task_edit_index,cur_user)

    
#Function printing user specific tasks, and saving them to a list
def print_user_specific_tasks_and_produce_list():
    loop_number = 1
    #print user specific tasks and saving them to a list
    user_spec_t_list = []
    for t in task_list:
        if t['username'] == current_user:
            print(f"\n{current_user}: Task {loop_number}")
            #creating a list containing elements for print_task function
            view_mine_print_list = [t['title'],t['username'],t['assigned_date'],t['due_date'],t['completed'],t['description']]
            print_task(view_mine_print_list)

            #This list stores a dictionary for each task the user has
            user_spec_t_list.append(t)
            loop_number += 1

    return user_spec_t_list


#Function asking to select a specific task to edit
def user_task_selection(u_spec_task_list):
    edit_number_validation = False

    while not edit_number_validation:
    #Ensuring an incorrect data type is not entered
        try:    
            u_t_edit_index = int(input("Enter the number of the task you wish to edit (If you don't wish to edit the task, enter -1): "))

        except ValueError as error:
            print(error)
            print("\nInvalid input. Please try again\n")
            continue

        '''
        After validation, we check the number, if it corresponds to one of the tasks, the user wishes to edit
        that specific task, so the edit_req(uest) is True and the boolean variable to break the loop is also True. 
        If the user does not wish to edit, entering -1, then the boolean variable to break the loop is True, but 
        edit_req is False. Any numbers will be invalid and the loop will continue
        '''
        if (u_t_edit_index >= 1) and (u_t_edit_index <= len(u_spec_task_list)):
            edit_number_validation = True
            edit_req = True
        elif (u_t_edit_index == -1):
            print("\nYou've chosen not to edit a task. You will now be returned to the options menu\n")
            edit_number_validation = True
            edit_req = False
        else:
            print("\nThe task number is outside the range. Please try again\n")

    #These variables are important for the next stages of the view_mine function
    return u_t_edit_index, edit_req


#Function dealing with all the variations when the user has requested to edit a task
def edit_user_specific_task(u_spec_t_list, task_to_edit_index,cur_user):
    user_change_task_input = user_input_string_validation("\n\nDo you wish to mark the task as complete or edit the task?\n", "Mark as complete", "Edit the task")
    #Get the task_list index for the task we wish to change 
    task_list_index = task_list.index(u_spec_t_list[task_to_edit_index - 1])

    if user_change_task_input == "Mark as complete":  #Condition 1: if the user has selected mark as complete
        #changing the completion status and then writing it to the text file
        task_list[task_list_index]['completed'] = "Yes"
        overwriting_task_txt()
        print("\nThe task has been marked as completed\n")
    else:                                   #Condition 2: if the user wishes to edit the task
        if task_list[task_list_index]['completed'] == "Yes": #Condtion A: If the task is completed, the user cannot edit
            print("\nThe task is already complete. You cannot edit the task. You will be returned to the options menu\n")
        else:    #Condition B: If the task isn't completed, it can be edited
                user_editing_choice = user_input_string_validation("\n\nDo you wish to change the user assigned to the task or the due date?\n", "Change user", "Change due date")
                        
                if user_editing_choice == "Change user": #Condtion I: If user wishes to change who the task is assigned to 
                    user_request_change_user_assigned_func(task_list_index,cur_user)
                else:                                       #Condition II: User wishes to change the due date
                    user_requested_change_due_date_func(task_list_index)     


#Function when the user has requested to change the user assigned to one of their tasks
def user_request_change_user_assigned_func(index,cur_user):
    user_validated = False

    while not user_validated:
        user_input_edit_user_assigned = input("\nEnter the name of the user you wish to assign this task to: ")

        if (user_input_edit_user_assigned in username_password.keys()) and (user_input_edit_user_assigned != cur_user):#NB: Exclude current user
            user_validated = True
        elif (user_input_edit_user_assigned in username_password.keys()) and (user_input_edit_user_assigned == cur_user):
            print("\nYou've entered your own username.\n")
            try_again_request = user_input_string_validation("Do you wish to try again? You will return to the options menu otherwise", "Y", "N")
            if try_again_request == "N": #if they don't wish to continue, the loop will break and the user sent back to the options menu
                break
        else:
            print("\nThe user does not exist in the database.\n")
            try_again_request = user_input_string_validation("Do you wish to try again? You will return to the options menu otherwise", "Y", "N")
            if try_again_request == "N": #if they don't wish to continue, the loop will break and the user sent back to the options menu
                break
                                
    if user_validated:
        task_list[index]['username'] = user_input_edit_user_assigned
        overwriting_task_txt()
        print("\nTask has been successfully edited.\n")


#Function editing the due date when requested by the user
def user_requested_change_due_date_func(index):
    new_due_date = task_due_date_validation()
    #New due date cannot be before the present date
    task_list[index]['due_date'] = new_due_date
    overwriting_task_txt()
    print("\nTask has been successfully edited.\n")


#=============================display statistics function========================

def display_stats():
    '''If the user is an admin they can display statistics about number of users
        and tasks, read from the overview text files. If the overview files are not found,
        then they are generated first, then read'''
    #If the two overview files don't exist, then call generate reports function
    if (not os.path.exists("task_overview.txt")) or (os.path.getsize("task_overview.txt") == 0):
        generate_reports()
    elif (not os.path.exists("user_overview.txt")) or (os.path.getsize("user_overview.txt") == 0):
        generate_reports()
    
    #Loop through the text files
    with open("task_overview.txt") as task_overview_file:
        for line in task_overview_file:
            #An empty line will contain "\n" only, which is 2 characters long
            #Any line with a length greater than 2 is not empty
            if len(line) > 2:
                print(line)
    
    #Create a gap
    print("\n\n")

    with open("user_overview.txt") as user_overview_file:
        for line in user_overview_file:
            if len(line) > 2:
                print(line)



#======================Generate reports============================

def generate_reports():
    generate_task_overview()
    generate_user_overview()
    print("\nThank you for generating the reports.\n")


def generate_task_overview():
    #Total_num tasks generated
    total_num_tasks_generated = len(task_list)
    #Now we must loop through the task list, to calculate the number of completed, uncomplete and overdue tasks
    num_completed_tasks = 0
    num_uncompleted_tasks = 0
    num_overdue_tasks = 0
    #To check if a task is overdue, we must compare it to the present date
    #https://www.geeksforgeeks.org/comparing-dates-python/
    present_date = datetime.now()
    for t in task_list:
        if t['completed'] == "Yes": #Condition 1: If task is marked as completed
            num_completed_tasks += 1
        else:   #Condition 2: If the task is marked as uncompleted
            num_uncompleted_tasks += 1
            #Any task overdue by definition must also be uncompleted
            if t['due_date'] < present_date: #Check if the task is overdue
                num_overdue_tasks += 1 
    
    #Calculate the two values using the division function
    percentage_tasks_incomplete = division(num_uncompleted_tasks, total_num_tasks_generated)
    percentage_tasks_overdue = division(num_overdue_tasks, total_num_tasks_generated)
    
    #Writing the data to the text file, creating the file if it didn't exist.
    generate_empty_txt_file("task_overview.txt")
    
    #Writing to the task_overview text file
    with open("task_overview.txt", "w") as task_overview_file:
        task_overview_file.write("==========================================\n")
        task_overview_file.write("\t\tTASK OVERVIEW\n\n")
        task_overview_file.write(f"Total number of tasks generated = {total_num_tasks_generated}\n\n")
        task_overview_file.write(f"Total number of completed tasks = {num_completed_tasks}\n")
        task_overview_file.write(f"Total number of uncompleted tasks = {num_uncompleted_tasks}\n")
        task_overview_file.write(f"Total number of overdue tasks = {num_overdue_tasks}\n\n")
        task_overview_file.write(f"Percentage of tasks incomplete = {percentage_tasks_incomplete} %\n")
        task_overview_file.write(f"Percentage of tasks overdue = {percentage_tasks_overdue} %\n")
        task_overview_file.write("==========================================\n")

    
def generate_user_overview():
    #Calculating some variables you wish to display
    total_num_users = len(username_password)
    total_num_tasks_generated = len(task_list)
           
    #Creating the text file if it doesn't exist
    generate_empty_txt_file("user_overview.txt")
    
    #writing to the user_overview text file
    with open("user_overview.txt", "w") as user_overview_file:
        user_overview_file.write("=====================================================================\n")
        user_overview_file.write("\t\t\tUSER OVERVIEW\n\n")
        user_overview_file.write(f"Total number of users registered = {total_num_users}\n")
        user_overview_file.write(f"Total number of tasks generate = {total_num_tasks_generated}\n\n")

        for user in username_password:
            user_overview_file.write(f"{user} REPORT:\n")
            user_specific_report(user, total_num_tasks_generated, user_overview_file)
            user_overview_file.write("---------------------------------------------------------------------")
            user_overview_file.write("\n\n")
        
        user_overview_file.write("=====================================================================\n")


#Generating the user specfic reports for the generate_user_overview function
def user_specific_report(a_user, tot_num_tasks, u_file):
    #Now we must loop through the task list, to calculate the number of completed, uncomplete and overdue tasks
    user_total_num_tasks = 0
    user_num_completed_tasks = 0
    user_num_uncompleted_tasks = 0
    user_num_overdue_tasks = 0
        #To check if a task is overdue, we must compare it to the present date
    #https://www.geeksforgeeks.org/comparing-dates-python/
    present_date = datetime.now()

    #Looping through the task lists, using conditions to calculate some variables we wish to display
    for t in task_list:
        if t['username'] == a_user:
            user_total_num_tasks += 1
            if t['completed'] == "Yes": #Condition 1: If task is marked as completed
                user_num_completed_tasks += 1
            else:   #Condition 2: If the task is marked as uncompleted
                user_num_uncompleted_tasks += 1
            #Any task overdue by definition must also be uncompleted
                if t['due_date'] < present_date: #Check if the task is overdue
                    user_num_overdue_tasks += 1 

    #Calculating some variables you wish to display, excepting zero division errors
    percentage_total_tasks_assigned_to_user = division(user_total_num_tasks, tot_num_tasks)
    percentage_user_tasks_completed = division(user_num_completed_tasks, user_total_num_tasks)
    percentage_user_tasks_uncompleted = division(user_num_uncompleted_tasks, user_total_num_tasks)
    percentage_user_tasks_overdue = division(user_num_overdue_tasks, user_total_num_tasks)
    
    #writing to the user_overview text file
    u_file.write(f"Total number of tasks assigned to user = {user_total_num_tasks}\n")
    u_file.write(f"Percentage of total number of tasks assigned to user = {percentage_total_tasks_assigned_to_user} %\n")
    u_file.write(f"Percentage of tasks assigned that have been completed = {percentage_user_tasks_completed} %\n")
    u_file.write(f"Percentage of tasks assigned that must still be completed = {percentage_user_tasks_uncompleted} %\n")
    u_file.write(f"Percentage of tasks assigned that are overdue = {percentage_user_tasks_overdue} %\n")


#Division function: When a zero division error occurs (eg dividing by num_tasks when there are no tasks), 
#the variable is set to zero
def division(a,b):
    try:
        #NB: Create a function for this
        c = round(((a/b)*100),2)
        
    except ZeroDivisionError as error_1:
        c = 0.00
    
    return c

#====================Program start=====================

#Enacting the file generating function if they don't already exist
generate_user_file()
generate_empty_txt_file("tasks.txt")

#Assigning a variable to the task list function
task_list = generate_task_list()

#Assigning a variable to the username_password function
username_password = create_username_password_dict()

#Login Section
login_status, current_user = login()

#Ensure that only logged in employees can access + manipulate the data
if login_status:
    '''
    menu must be defined before we can have it as a condition for the while loop, 
    but we don't want it as any of the actual options
    '''
    menu = "x"
    '''Whilst the user has not selected the exit option, the loop continues, until the user
    selects the exit option ('e')
    As we have added to option to change the user, if they choose not to login again, the loop breaks
    and the program ends'''
    while menu != "e" and login_status:
        # presenting the menu to the user 
        menu = menu_options()

        if menu == 'r': #Change to admin only (Mentor suggestion)
            if current_user == 'admin': 
                reg_user() 
            else:
                print("You don't have authority to register a user. Please select another option\n")      
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all()            
        elif menu == 'vm':
            view_mine(current_user)    
        elif menu == 'ds': 
            if current_user == 'admin': 
                display_stats()
            else:
                print("You don't have authority to display the statistics. Please select another option\n")
        elif menu == "gr": #Change to admin only
            if current_user == 'admin': 
                generate_reports() 
            else:
                print("You don't have authority to generate reports. Please select another option\n") 
        elif menu == "cu":
            login_status, current_user = login()
        else:            #Here, menu = "e" 
            print('\nThank you for using the program\n')