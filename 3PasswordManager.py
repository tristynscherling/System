import csv
import secrets
import string
from pathlib import Path

ACCOUNT_FILE = Path("account_info.csv")
MIN_PASSWORD_LENGTH = 12
MAX_PASSWORD_LENGTH = 64
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL_CHARACTERS = "!@#$%^&*()-+"
ALL_CHARACTERS = LOWERCASE + UPPERCASE + DIGITS + SPECIAL_CHARACTERS


def read_accounts():
    if not ACCOUNT_FILE.exists():
        return []

    with ACCOUNT_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def validate_password(password):
    return (
        MIN_PASSWORD_LENGTH <= len(password) <= MAX_PASSWORD_LENGTH
        and any(character in LOWERCASE for character in password)
        and any(character in UPPERCASE for character in password)
        and any(character in DIGITS for character in password)
        and any(character in SPECIAL_CHARACTERS for character in password)
    )


def generate_password(length):
    password_characters = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SPECIAL_CHARACTERS),
    ]
    password_characters.extend(
        secrets.choice(ALL_CHARACTERS) for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    password = "".join(password_characters)
    if not validate_password(password):
        raise RuntimeError("Generated password did not meet the strength requirements.")
    return password


def mask_password(password):
    return "*" * len(password)


def add_account():
    account_name = input("Enter account name: ").strip()
    username = input("Enter account username: ").strip()
    if not account_name or not username:
        print("Account name and username cannot be empty.")
        return

    length_text = input(
        f"Password length ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}): "
    ).strip()
    try:
        length = int(length_text)
    except ValueError:
        print("Please enter a whole-number password length.")
        return

    if not MIN_PASSWORD_LENGTH <= length <= MAX_PASSWORD_LENGTH:
        print(
            f"Password length must be between "
            f"{MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH}."
        )
        return

    password = generate_password(length)
    if any(account["password"] == password for account in read_accounts()):
        print("A duplicate password was generated. Please try again.")
        return

    file_exists = ACCOUNT_FILE.exists()
    with ACCOUNT_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["account_name", "username", "password"]
        )
        if not file_exists or ACCOUNT_FILE.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(
            {
                "account_name": account_name,
                "username": username,
                "password": password,
            }
        )

    print(f"Account saved. Generated password: {password}")


def display_accounts(accounts=None):
    if accounts is None:
        accounts = read_accounts()

    if not accounts:
        print("No stored accounts found.")
        return

    print("\nStored accounts:")
    for account in accounts:
        print(
            f"Account: {account['account_name']}, "
            f"Username: {account['username']}, "
            f"Password: {mask_password(account['password'])}"
        )


def search_accounts():
    query = input("Search by account name or username: ").strip().casefold()
    matches = [
        account
        for account in read_accounts()
        if query
        and (
            query in account["account_name"].casefold()
            or query in account["username"].casefold()
        )
    ]
    display_accounts(matches)


def main():
    print("Welcome to the Password Manager!")
    while True:
        print("\n1. Generate and save a password")
        print("2. View stored accounts")
        print("3. Search accounts")
        print("4. Exit")
        option = input("Choose an option: ").strip()

        if option == "1":
            add_account()
        elif option == "2":
            display_accounts()
        elif option == "3":
            search_accounts()
        elif option == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
