from datetime import date
from uuid import uuid4
import json


class Member:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        password: str,
        membership=None,
        id=None,
        is_admin=None,
        membership_date=None,
    ):
        self.id = str(uuid4()) if id is None else id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.membership = "regular" if membership is None else membership
        self.is_admin = False if is_admin is None else bool(is_admin)
        self.membership_date = (
            str(date.today()) if membership_date is None else membership_date
        )

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"<Member {self.fullname},{self.email}, member since {self.membership_date}>"

    def __repr__(self):
        return f"<Member {self.id} {self.fullname}, {self.age}, {self.email}>"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
