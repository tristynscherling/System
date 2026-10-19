# Constants for limits
MIN_NAME_LENGTH = 3
run = True

def optionchoicer():
    print("Welcome to the Username Generator!")
    option = input("Enter 1 to generate a username, 2 to view usernames, or 3 to exit: ")
    option = option.strip().replace(" ", "")
    try:
        if option not in ["1", "2", "3"]:
            print("Invalid option. Please try again.")
            return optionchoicer()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return optionchoicer()
    return option

option = optionchoicer()

while run == True:
    if option == "1":
        # Ask the user for their first and last name
        userFirstname = input("Enter your first name: ")
        userLastname = input("Enter your last name: ")
        # Generate the username by concatenating the first letter of the first name with the last name
        # and strip it of any whitespace and convert it to lowercase
        userFirstname = userFirstname.strip()
        userLastname = userLastname.strip()
        userFirstname = userFirstname.replace(" ", "")
        userLastname = userLastname.replace(" ", "")
        username = userFirstname[0].lower() + userLastname.lower()
        print("Your username is:", username)
        # Validate that names meet a minimum length requirement
        if len(userFirstname) < MIN_NAME_LENGTH or len(userLastname) < MIN_NAME_LENGTH:
            print("Error: First and last names must be at least 3 characters long.")
            continue
        # Make sure that the usernames.txt file exists and create it if it doesn't
        try:
            with open("usernames.txt", "r") as file:
                pass
        except FileNotFoundError:
            with open("usernames.txt", "w") as file:
                pass

        # Make sure the username is unique by checking against a list of existing usernames
        with open("usernames.txt", "r") as file:
            existing_usernames = file.read().splitlines()
        if username in existing_usernames:
            print("Error: Username already exists.")
            continue
        #Save username to a file
        with open("usernames.txt", "a") as file:
            file.write(username + "\n")
        optionchoicer()

    if option == "2":
        # Ask the user if they want to see all usernames make sure it returns to the optionchoicer() function if they don't want to see the usernames
        view_usernames = input("Do you want to see all usernames? (y/n): ")
        if view_usernames == "y":
            with open("usernames.txt", "r") as file:
                print("All usernames:")
                for line in file:
                    print(line.strip()) 
        optionchoicer()

    if option == "3":
        print("Exiting the program.")
        run = False
        