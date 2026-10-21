import math
import random

# Constants
strictness = 3
complexity = 3
min_length = 8
max_length = 24
special_enabled = True
special_characters = "!@#$%^&*()-+"

# Validate the password meets the strictness and complexity requirements

def validate_password(password):
    return (
        len(password) >= min_length and
        len(password) <= max_length and
        sum(1 for c in password if c.islower()) >= strictness and
        sum(1 for c in password if c.isupper()) >= strictness and
        sum(1 for c in password if c.isdigit()) >= complexity and
    sum(1 for c in password if c in special_characters) >= complexity
)

# Generate password using random module and the constants defined above
def generate_password():
    # Characters to use in the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+"
    # Filler variable to hold the password
    password = ""
    # Generation using range and random.choice to select characters from the characters string
    for _ in range(random.randint(min_length, max_length)):
        password += random.choice(characters)
    return password
    # Make sure the password meets the strictness and complexity requirements else, generate a new password
    if not validate_password(password):
        return generate_password()
    else:
        return password



# Store; Account name, Username, and Password in a file

# Check if the account_info.txt file exists and create it if it doesn't
try:
    with open("account_info.txt", "r") as file:
        pass
except FileNotFoundError:
    with open("account_info.txt", "w") as file:
        pass

def store_account_info(account_name, username, password):
    with open("account_info.txt", "a") as file:
        file.write(f"{account_name},{username},{password}\n")

# Search for stored accounts.
def search_accounts(account_name=None, username=None):
    accounts = []
    try:
        with open("account_info.txt", "r") as file:
            for line in file:
                name, user, pwd = line.strip().split(",")
                if (account_name is None or name == account_name) and (username is None or user == username):
                    accounts.append((name, user, pwd))
    except FileNotFoundError:
        pass
    return accounts

# Check for duplicate passwords in the stored accounts.
def check_duplicate_passwords():
    passwords = set()
    duplicates = set()
    try:
        with open("account_info.txt", "r") as file:
            for line in file:
                _, _, pwd = line.strip().split(",")
                if pwd in passwords:
                    duplicates.add(pwd)
                else:
                    passwords.add(pwd)
    except FileNotFoundError:
        pass
    return duplicates

# Mask passwords when displaying them to the user. 
def mask_password(password):
    return '*' * len(password)



