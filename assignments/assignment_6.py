# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
import json
import pickle

file_contents = []

def write_to_file():
    with open('assignment_6.txt', mode='w') as f:
        f.write(json.dumps(file_contents))
        f.write('\n')

    print('Write Complete!')

def print_from_file():
    with open('assignment_6.txt', mode='r') as f:
        file_content = f.readlines()
        print(file_content)
    
    print('Read Complete!')

def build_list():
    user_text = input('Enter your string: ')
    file_contents.append(user_text)

input_state = True
while input_state:
    print('1. Enter your string')
    print('2. Read from the file')
    print('x. Quit')
    user_input = input('Enter your choice: ')

    if user_input == '1':
        build_list()
        write_to_file()
    elif user_input == '2':
        print_from_file()
    elif user_input == 'x':
        input_state = False
    else:
        print('Give a valid input, please!!')

print("Program Completed!")


# 4) Adjust the logic to load the file content to work with pickled/ json data.
