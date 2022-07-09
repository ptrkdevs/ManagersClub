from member import Member
from typing import List
import json


from exceptions import PasswordIncorrectError, MemberNotFoundError


def validate_credentials(
    email: str, password: str, membersList: List[Member]
) -> Member:

    member_found = None

    # validate user credentials
    for member in membersList:
        if member.email == email:

            member_found = member

    # check if email has matched
    if not member_found:
        raise MemberNotFoundError(f"Member with email {email} not found")

    # check password
    if member_found.password == password:
        return member_found

    raise PasswordIncorrectError(f"Password incorrect")


def get_credentials(form):
    """gets the user input for logging in and register"""

    if form == "login":
        email = input("Email: ")
        password = input("Password: ")

        return {"email": email, "password": password}

    else:
        firstname = input("firstName: ")
        lastname = input("lasttName: ")
        age = int(input("Age: "))
        email = input("Email: ")
        password = input("Password: ")

        return {
            "first_name": firstname,
            "last_name": lastname,
            "age": age,
            "email": email,
            "password": password,
        }


def get_db():

    try:
        with open("db.json") as db:
            return json.load(db)

    except FileNotFoundError:
        return []


# save to json
def save_to_db(member):

    # get json db
    membersList = get_db()

    membersList.append(member.toJSON())

    # # serialize members dict
    members_obj = json.dumps(membersList)

    with open("db.json", "w") as db:
        db.write(members_obj)


data = [Member(**json.loads(member)) for member in get_db()]

print(data)
