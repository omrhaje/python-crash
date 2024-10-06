# os is operating system
import os

file_path = "56.1.test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That's a directory")
else:
    print("The location doesn't exists")