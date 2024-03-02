""" View """


def show_all_view(users: list[dict[str, str]]):
    print(f"In database, total users are {users.__len__()}.")
    for item in users:
        print(item)


def start_view():
    print("MVC - Simple example.")
    print("Do you want to see anyone in database? [Y/N]")


def end_view():
    print("Goodbye.")
