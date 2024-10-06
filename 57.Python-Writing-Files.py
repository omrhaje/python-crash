# Python writing files (.txt, .json, .csv)                      # w = write      a = append

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]      # <-- .txt

import json
import csv

employees1 = [["Name", "Age", "Job"],
             ["Spongebob", 26, "Cook"],
             ["Patrick", 25, "Janitor"],            # <-- .csv
             ["Squidward", 31, "Cashier"]]

employee = {
    "name": "Spongebob",
    "age": 30,                    # <-- .json
    "job": "Cook"
}

file_path = "/Users/omarhaje/FILEs/DEV/output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees1:
            writer.writerow(row)
        print(f"csv file {file_path} was created!")
except FileExistsError:
    print("File already exists!")