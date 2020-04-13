"""
TODO
1. Find all CSV files in cwd
2. Read contents of each file
3. Skip first line and write contents to new CSV file
"""

import csv
import os

#changes directory to location of desired csv files
csv_location_folder = input('Input the directory containing the CSV files:')
os.chdir(csv_location_folder)

#creates new directory for resulting csv files
os.makedirs('headerRemoved', exist_ok = True)


for csvFilename in os.listdir('.'): #loops through all filed in current dir
    if not csvFilename.endswith('.csv'): #skips a file if it does not have csv extension
        continue

    print('Removing header from' +csvFilename+ '...') #shows what file is being worked on

#Takes data without header
    csvRows = []
    csv_file = open(csvFilename)
    read_csv = csv.reader(csv_file)
    for row in read_csv:
        if read_csv.line_num == 1:
            continue
        csvRows.append(row)
    csv_file.close()


#Write data to file without header
    csv_file = open(os.path.join('headerRemoved', csvFilename), 'w', newline = '')
    csv_write = csv.writer(csv_file)
    for row in csvRows:
        csv_write.writerow(row)
    csv_file.close()
