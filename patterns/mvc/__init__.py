""" Controller """
import view
from model import PersonDatabase


def show_all():
    person = PersonDatabase()
    persons = person.get_all_users()
    return view.show_all_view(persons)


def start():
    view.start_view()
    question = input()
    if question in ("y", "Y"):
        return show_all()
    else:
        return view.end_view()


if __name__ == "__main__":
    start()
