"""
TODO:
1. Create a regex for phone numbers (Done)
2. Create a regex for email addresses
3. Get the text off the clipboard
4. Extract the email/phone from text
5. Copy extracted email/phone to clipboard
"""

import re
import pyperclip

#1. Create regex for phone numbers

name_template = re.compile(r'''
([A-Z][a-z]+\n?#first name
(\s+)?#middle space
[A-Z][a-z]+)#last name
''',re.VERBOSE)

phone_template = re.compile(r'''
# 000-000-0000, 111-1111, (222) 222-2222, 333-3333 ext 12345, ext. 12345, x12345
(
((\d\d\d) | (\(\d\d\d\)))?     # area code: optional
(\s|-)                         # first separator
\d\d\d                         # first 3 digits
-                              # separator
\d\d\d\d                       # last 4 digits
(((ext(\.)?\s | x)             # extension word or letter: optional
(\d){2,5}))?)                    #extension number
''',re.VERBOSE)

#2. Create regex for email addresses
email_template = re.compile(r'''
[a-zA-Z0-9_.+]+    #name (spaces not used in email)
@                  #at symbol (special character)
[a-zA-Z0-9_.+]+    #domain name

''', re.VERBOSE)

#3. Get text from cliboard
text_from_clipboard = pyperclip.paste()

#4. Extract email/phone from text
extracted_phone = phone_template.findall(text_from_clipboard)
extracted_email = email_template.findall(text_from_clipboard)
extracted_name = name_template.findall(text_from_clipboard)

phone_numbers = []
all_names = []
for phone in extracted_phone:
    phone_numbers.append(phone[0])

for item in extracted_name:
    all_names.append(item[0])


#5. Copy extracted email/phone TO clipboard
return_both = []
for i in range(len(all_names)):
    return_both[i].append(''.join(all_names[i]) + '  ' + ''.join(phone_numbers) + '   ' + ''.join(extracted_email))
pyperclip.copy(return_both)
