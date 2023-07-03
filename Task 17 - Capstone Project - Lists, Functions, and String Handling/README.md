# Task manager


## Table of Contents
===================

  * [Project description](#Project-description)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Credits](#credits)


## Project description
The original program could register a user, add a task, view all tasks, view logged-in user's task and display basic task statistics. 
The requirements where to improve readability via abstraction, allow the logged-in user to edit one of their tasks (change due date or mark as complete) and generate user + task overviews. The original code also required validation for all existing choices to prevent user inputs causing errors. Some options where changed to admin only, so the option to change the logged-in user was additionally added.

## Installation
This program requires no additional packages to be installed

## Usage
When the program starts, the user is required to login. If this is successful, the user is presented with all the options available:
![Program start](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20program%20start.png)


* Registering a user: This is an admin only option, so only if the user is logged-in as admin will they be able to select this option. Here, the user is asked to enter the username and the password is asked for twice to confirm. If the username does not already exist AND the two passwords match, then the username and password are written to the user.txt file.
  * Entering non-matching passwords, then entering matching passwords
    ![registering a user](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20register%20a%20user.png)
  
  * Username and password added to user.txt
    ![Add user to txt file](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20register%20a%20user%20txt%20file.png)

  * If the current user is not 'admin', the selection fails and the user is returned to the option menu
    ![Admin only fail](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20admin%20specific%20option%20fail.png)


* Adding a task: This can be selected by any user, with the user and date being validated, ensuring the user already exists and the due date is after the present date.
  * Entering some valid and invalid inputs
    ![Adding a task part 1](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20add%20a%20task%20part%201.png)

  * After successfully entering the inputs, the whole task is displayed in the standard terminal format
    ![Adding a task part 2](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20add%20a%20task%20part%202.png)

  * The task is then added to tasks.txt in the format specific to that file
    ![Add task to txt file](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20add%20a%20task%20txt%20file.png)


* View all tasks: This displays every single task, assigned to any user. The tasks are displayed in the standard terminal format.
  ![View all](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20view%20all.png)


* View my tasks: 
  * Displays all the tasks of the current user. The user is given the option to select a task to edit
    ![View mine](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20view%20mine%20initial.png)

  * Selecting a specific task, entering incorrect inputs to show how they are dealt with
    ![Editing a task](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20view%20mine%20next.png)

  * Entering -1 ensures no tasks are edited and returns the user to the options menu
    ![exiting view mine](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20view%20mine%20exit.png)


* Generate reports: This option generates two reports as txt files, the task overview and the user overview. 
 1. Task Overview: A general overview on the number of tasks, completed, incomplete and overdue.
    ![Task overview txt](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20generating%20reports%20task%20overview.png)

  2. User overview: Gives a general overview of the number of users and tasks. Then for each user, it gives a break down of their tasks, in a format similar to task overview.
    ![user overview](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20generating%20reports%20user%20overview.png)


* Display statistics: This gets all the data from user overview and task overview and prints it to the terminal. If the overviews have not been generated, it generates them first, then displays the reports in the terminal.
  ![ds part 1](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20display%20statistics%20part%201.png)
  ![ds part 2](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20display%20statistics%20part%202.png)
  ![ds part 3](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20display%20statistics%20part%203.png)


* Change user: As some options are admin only, this option was added. 
  ![change user](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20change%20user.png)


* Exit: Once the user has finished using the program, they need to be able to end the loop and the program. 
  ![exit](https://github.com/ia-siddiqui/finalCapstone/blob/main/Task%2017%20-%20Capstone%20Project%20-%20Lists%2C%20Functions%2C%20and%20String%20Handling/Usage%20photos/Task%20manager%20exit.png)



## Credits
Author(s): [Ibraheem Siddiqui](https://github.com/ia-siddiqui)

Client: HyperionDev DfE Software Engineering (Fundamentals) Bootcamp
