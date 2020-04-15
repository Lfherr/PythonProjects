"""Opens websites based on a url in a text file. Opens each website in a different tab.
Text file destination is provided by user"""


import webbrowser

def file_len(file_name):
    len_count = 0
    use_file = open(file_name)
    for i in enumerate(use_file):
        len_count += 1
    return len_count


def open_it(site):
    webbrowser.get(chrome_path).open_new_tab(site)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
input_file = input('Enter File Destination: ')
sites_len = file_len(input_file)
files_to_use = open(input_file)
sites = files_to_use.readlines()

for i in range(sites_len):
    current_url = sites[i].rstrip()
    open_it(current_url)

