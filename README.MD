# Note-Me
A simple notes app that uses Vim (VI Improved) as his default editor and stores the notes on a git repo.

## Installation
First clone/download this repo.

You should then add the **.config/note-me/** folder to the **~/.config/** folder.

You need to have Python for this to work (it should be installed if you are on linux). After installing Python if you want to use the **copy/paste** features you should install the **pyperclip** package:

```
pip3 install pyperclip
```
You could run this from the terminal by switching to the path of the cloned repo, but for facilitating it's use you should add this line to your **.bashrc** file:
```bash
alias noteme="cd path/to/this/repo && python3 noteme.py"
```

If you are using (Neo)Vim, you can install the plugin [Note Me Vim](https://github.com/Force4760/note-me-vim) that I created to hel users with this

### Create Git Repo
On the **/Notes** folder run the following commands:
```bash
git init

git commit -m "first commit"

git branch -M main

git remote add origin https://link/to/the/remote/git/repo

git push -u origin main
```

## Use
This script gives you several flags that can be used to make the script work in different ways.

- noteme
    
    - running the script without any arguments a daily note (following the date_template.md template) if it does not already exist, else it will add the hour of the day as **### hour:day**

- noteme -notename*
    
    - running the script with the **-notename*** flag, a non daily note will be created/opened (according to if it exists or not) with the name **notename.md**, following the **non_date_template.md** file

- noteme -t

    - running with the **-t** flag the **todo.md** file will be opened

- noteme -p

    - running with the **-p** flag the current clipboard contents will be pasted as a new entry on the current daily note

- noteme -v

    - running with the **-v** flag the current daily note will be converted to an html page and opened with your default browser.

- noteme -vt

    - running with the **-vt** flag the todo note will be converted to an html page and opened with your default browser.

- noteme -v day/month/year

    - running with the **-v day/month/year** flag the specified daily note will be converted to an html page and opened with your default browser.

- noteme -v -notename*

    - running with the **-v -notename*** flag the specified non daily note will be converted to an html page and opened with your default browser.

- noteme -p -notename*

    - running with the **-p -notename*** flag the current clipboard content will be pasted as a new entry on the **notename.md** file

## Configure

This app allows you to make some changes to the default configuration. 

- noteme -s

    - running the **-s** flag you will be prompted with the various options for the **settings.json** file:

        - editor (string)(editor to use when opening the notes)
        - git (boolean) (if the app should use git)
        - base (string)(the path to the base folder of the notes)

You can also edit the templates in **~/.config/note-me/templates** to change the default note for daily and non-daily notes.
