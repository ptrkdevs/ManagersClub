import enum
from member import Member

import json


from exceptions import PasswordIncorrectError, MemberNotFoundError


def validate_credentials(email: str, password: str) -> Member:

    member_found = None

    membersList = get_db()

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
            data = json.load(db)
            return [Member(**json.loads(member)) for member in data]

    except FileNotFoundError:
        return []


def save(membersList):
    # serialize members dict
    members_obj = json.dumps(membersList)

    with open("db.json", "w") as db:
        db.write(members_obj)


# save to json
def save_to_db(member: Member, edit: bool, db=None):

    # get json db
    membersList = get_db() if db is None else db

    if not edit:

        membersList.append(member.toJSON())

        save(membersList)
        return member

    else:
        for index, _member in enumerate(membersList):
            if _member.id == member.id:
                membersList.pop(index)

        save_to_db(member, edit=False, db=membersList)


def delete_user(member: Member):

    db = get_db()

    for index, _member in enumerate(db):
        if _member.id == member.id:
            db.pop(index)

    save(db)
