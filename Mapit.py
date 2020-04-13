import sys
import pyperclip
import webbrowser

sys.argv #collects argument from command line,  no () because it is a variable, not function

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) #join elements of list

else:
    address = pyperclip.paste()

webbrowser.open_new_tab('https://www.google.com/maps/place/' + address)