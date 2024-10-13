# Python reading files (.txt, .json, .csv)

file_path = "/Users/omarhaje/FILEs/DEV/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()                               # <-- How to read a .txt file
        print(content)
except FileNotFoundError:
    print("That file was not found!")


import json

file_path = "/Users/omarhaje/FILEs/DEV/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)                          # <-- How to read a .json file
        print(content["job"])                              # If needed to access a column, type in the print statement [] and a str of your choice
except FileNotFoundError:
    print("That file was not found!")


import csv

file_path = "/Users/omarhaje/FILEs/DEV/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)                      # <-- How to read a .csv file
        for line in content:
            print(line[2])                                 # If needed to access a specified column, type in the print statement [] and an int of your choice
except FileNotFoundError:
    print("That file was not found!")