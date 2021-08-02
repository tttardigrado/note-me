import json
import os


def set_settings():
    with open(os.path.expanduser("~/.config/note-me/settings.json"), "r") as f:
        data = json.load(f)

        e = input(f"Editor: ")
        g = input(f"Execute git (y/n): ")
        b = input(f"Base Folder: ")

        if e:
            data["editor"] = e

        if g == "yes" or g == "y" or g == "Yes" or g == "Y":
            data["git"] = True
        else:
            data["git"] = False
        
        if b:
            data["base"] = b

    os.remove(os.path.expanduser("~/.config/note-me/settings.json"))
    with open(os.path.expanduser("~/.config/note-me/settings.json"), "w") as f:
        json.dump(data, f, indent=4)
