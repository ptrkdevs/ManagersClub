from exceptions import MemberNotFoundError, PasswordIncorrectError
from utils import get_credentials, validate_credentials, save_to_db, delete_user
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


def membersMenu(*args):

    members_menu = """
    _______***_______
        1. View my details
        2. Edit details
        3. Delete my Account
        4. Exit
    _______***_______
    """
    print(members_menu)
    while (choice := input("Choice: ")) not in ["1", "2", "3", "4"]:
        print(members_menu)

    if choice == "1":
        get_member_details(*args)
    elif choice == "2":
        edit_user_details(*args)
    elif choice == "3":
        delete_user_account(*args)
    elif choice == "4":
        print("Thank you for check in, have a nice day")


# member details
def get_member_details(member: Member):

    print(
        f"""
        FullName: {member.fullname}
        Email: {member.email}
        FirstName: {member.first_name}
        LastName: {member.last_name}
    """
    )
    membersMenu(member)


def delete_user_account(member: Member):

    try:
        delete_user(member)
    except:
        print('something went wrong')
    else:
        menu()

def edit_user_details(member):

    first_name = input("FirstName: ")
    last_name = input("LastName: ")
    email = input("Email: ")

    if first_name == "":
        first_name = member.first_name

    if last_name == "":
        last_name = member.last_name
    if email == "":
        email = member.email

    member.first_name = first_name
    member.last_name = last_name
    member.email = email

    save_to_db(member=member, edit=True)


def register():

    print("Join us today, Please enter following user details")

    user_input = get_credentials("register")

    member = Member(**user_input)

    save_to_db(member, edit=False)

    print("All abord to our club!")

    membersMenu(member)


def login():

    user_input = get_credentials("login")

    # verify user credentials
    try:
        member = validate_credentials(**user_input)
    except PasswordIncorrectError as e:
        print(e)
    except MemberNotFoundError as e:
        print(e)
    else:
        print(f"Welcome back {member.first_name}")
        membersMenu(member)


if __name__ == "__main__":
    welcome()
    menu()
