import math
import random

# Constants
strictness = 3
complexity = 3
min_length = 8
max_length = 24

validate_password = lambda password: (
    len(password) >= min_length and
    len(password) <= max_length and
    sum(1 for c in password if c.islower()) >= strictness and
    sum(1 for c in password if c.isupper()) >= strictness and
    sum(1 for c in password if c.isdigit()) >= complexity and
    sum(1 for c in password if c in "!@#$%^&*()-+") >= complexity
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
