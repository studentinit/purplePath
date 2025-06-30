
# FILE + IO ERRORS:
# here is a simple script to access files to read, write, append.
# for demonstrating error handling stucture in a try/except block.
#-----------------------------------------#

# get target info
file = input("enter filename you want to access: ")

# get contents info
word = input("what are adding or we looking for?: ")

# get mode info
action = input("are we reading, writing, or appending?: ")
if action == "read" or action == "reading":
    mode = "r"
elif action == "write" or action == "writing":
    mode = "w"
elif action == "append" or action == "appending":
    mode = "a"

try:
    with open(file, mode) as f:
        if mode == "r":
            for _ in f:
                if word in _:
                    print("\n", _)
        elif mode == "w" or mode == "a":
            f.write(f"{word}\n")
except FileNotFoundError:  
    print("the file you are trying to access does not exist") 
