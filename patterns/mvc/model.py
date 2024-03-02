""" Model """


class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class PersonDatabase:
    def __init__(self) -> None:
        pass

    def get_all_users(self) -> list[dict[str, str]]:
        with open("./design_patterns/mvc/database.txt", mode="r") as database:
            raw_data: str = database.read()
        return [self.split_user(user) for user in raw_data.split("\n")]

    def split_user(self, user: str):
        first_name, last_name = user.split(" ")
        return {"first_name": first_name, "last_name": last_name}
