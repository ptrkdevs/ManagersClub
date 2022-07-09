from exceptions import MemberNotFoundError, PasswordIncorrectError
from utils import get_credentials, validate_credentials, save_to_db
from member import Member

members_list = []


def welcome():
    print("Welcome to People Managers club")


def menu():
    menu_message = """ 
    _______***_______
        1. Log in
        2. View Membership details
        3. Register
        4. Exit
    _______***_______
    """
    print(menu_message)

    while (choice := input("Choice: ")) not in ["1", "2", "3", "4"]:
        print(menu_message)

    if choice == "1":
        login()
    elif choice == "2":
        print("user input 2")
    elif choice == "3":
        register()
    elif choice == "4":
        print("Thank you for check in, have a nice day")


def membersMenu():
    pass


def register():

    print("Join us today, Please enter following user details")

    user_input = get_credentials("register")

    member = Member(**user_input)

    save_to_db(member)

    print("All abord to our club!")

    menu()


def login():

    user_input = get_credentials("login")

    # verify user credentials
    try:
        member = validate_credentials(**user_input, membersList=members_list)
    except PasswordIncorrectError as e:
        print(e)
    except MemberNotFoundError as e:
        print(e)
    else:
        print(f"Welcome back {member.first_name}")


if __name__ == "__main__":
    welcome()
    menu()
