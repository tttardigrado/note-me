import os
from . import day


def check(b: str):
    """
    Check if the notes folder exists
    b: str -> base folder
    """
    # check if notes folder exists
    folder = b + "Notes/"
    make_d(folder)

    # get date
    date = day.get_date(False)

    # check if year folder exists
    folder = folder + str(int(date[2]))
    make_d(folder)

    # check if month folder exists
    folder = folder + "/" + str(int(date[1]))
    make_d(folder)

    return folder


def check_next(b: str):
    """
    Check if the notes folder exists
    b: str -> base folder
    """
    # check if notes folder exists
    folder = b + "Notes/"
    make_d(folder)

    # get date
    date = day.get_date_next()

    # check if year folder exists
    folder = folder + str(int(date[2]))
    make_d(folder)

    # check if month folder exists
    folder = folder + "/" + str(int(date[1]))
    make_d(folder)

    return folder


def make_d(folder: str):
    """Check if a folder exists, if not then create it

    Args:
        folder (str): the folder to check
    """
    if not os.path.exists(folder):
        os.mkdir(folder)


if __name__ == "__main__":
    check_next("home/force/Documents/")

