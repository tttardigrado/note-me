import os
import functions.check_folder as check_folder
import functions.day as day
import datetime


def file_edit(file: str, date: list, hour: list):
    """
    file: str -> the file where the note is going to be taken
    date: list -> a list [day, month, year]
    hour: list -> a list [day, hour, minute]
    """
    if not os.path.exists(file):
        dont_exists(file, date, hour)
    else:
        exists(file, date, hour)


def dont_exists(file: str, date: list, hour: list):
    """
    If the file does not exist

    file: str -> the file where the note is going to be taken
    date: list -> a list [day, month, year]
    hour: list -> a list [day, hour, minute]
    """
    with open(file, "w") as f:
        d = "# " + date[0] + "/" + date[1] + "/" + date[2] + "\n"
        if os.path.exists(os.path.expanduser("~/.config/note-me/templates/non_date_template.md")):
            with open(os.path.expanduser("~/.config/note-me/templates/date_template.md"), "r") as t:
                template = "\n" + t.read() + "\n"
        else:
            template = ""
        h = "\n### " + hour[1] + ":" + hour[2] + "\n"
        f.write(d + template + h)


def exists(file: str, date: list, hour: list):
    """
    If the file exists

    file: str -> the file where the note is going to be taken
    date: list -> a list [day, month, year]
    hour: list -> a list [day, hour, minute]
    """
    with open(file, "a") as f:
        h = "### " + hour[1] + ":" + hour[2]
        f.write("\n\n" + h + "\n")


def copy(file, w: str):
    """
    Paste w to file

    file: str -> file to write
    w: str -> what to write
    """
    with open(file, "a") as f:
        f.write(w)


def note_file(b: str, w: str = "", n: bool = False):
    """
    Prepare note
    s: str -> base path
    w: str -> if given it will be written to the file. (optional)
    """
    if n:
        # check folder
        folder = check_folder.check_next(b)
    
        # get date
        hour = day.get_hour_next()
        date = day.get_date_next()
    else:
        # check folder
        folder = check_folder.check(b)
    
        # get date
        hour = day.get_date(True)
        date = day.get_date(False)



    file = folder + "/" + str(int(hour[0])) + ".md"

    file_edit(file, date, hour)
    if w:
        copy(file, w)
    return file
