""" Sets google maps to give directions to given address
"""

import sys
import pyperclip
import webbrowser

sys.argv                #collects argument from command line

if len(sys.argv) > 1:   #Excludes script name
    address = ' '.join(sys.argv[1:]) #join elements of list

else:                   #Alternative is grab address from clipboard
    address = pyperclip.paste()

#Opens google maps with address attached.
webbrowser.open_new_tab('https://www.google.com/maps/place/' + address)
