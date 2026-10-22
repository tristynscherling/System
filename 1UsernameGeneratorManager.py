USERNAME_FILE = "usernames.txt"
MIN_NAME_LENGTH = 3


def read_usernames():
    try:
        with open(USERNAME_FILE, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def add_username():
    first_name = input("Enter first name: ").strip().replace(" ", "")
    last_name = input("Enter last name: ").strip().replace(" ", "")

    if len(first_name) < MIN_NAME_LENGTH or len(last_name) < MIN_NAME_LENGTH:
        print(f"First and last names must be at least {MIN_NAME_LENGTH} characters.")
        return

    username = (first_name[0] + last_name).lower()
    usernames = read_usernames()

    if username in usernames:
        print("That username already exists.")
        return

    with open(USERNAME_FILE, "a", encoding="utf-8") as file:
        file.write(username + "\n")
    print("Saved username:", username)


def view_usernames():
    usernames = read_usernames()
    if not usernames:
        print("No usernames found.")
        return

    for username in usernames:
        print(username)


def search_username():
    search = input("Enter a username to search for: ").strip().lower()
    usernames = read_usernames()
    found = False

    for username in usernames:
        if search and search in username.lower():
            print(username)
            found = True

    if not found:
        print("Username not found.")


def main():
    while True:
        print("\n1. Create username\n2. View usernames\n3. Search usernames\n4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_username()
        elif choice == "2":
            view_usernames()
        elif choice == "3":
            search_username()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
