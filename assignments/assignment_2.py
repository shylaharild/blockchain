username_list = []


def get_username():
    """Fuction to get the username as an input.
    Returns the given username.
    """
    return input("Give me a name: ")


def print_given_name():
    """Prints the name from the list.

    Uses 'for' loop to get each name from list.
    It also checks the length of each name and outputs the name that as 5 or more characters in it.

    Also checks if name has character 'n' or 'N' in it
    """
    for name in username_list:
        # 1) Create a list of names and use a for loop to output the length of each name (len()).
        name_len = len(name)
        print("Length of the name " + name + " is " + str(name_len))

        # 2) Add an if check inside the loop to only output names longer than 5 characters.
        if name_len >= 5:
            print("The name which has 5 or more character is " + name)

        # 3) Add another if check to see whether a name includes a “n” or “N” character.
        if 'n' in name or 'N' in name:
            print("The name includes character n or N in it!")


# 4) Use a while loop to empty the list of names (via pop())
def pop_last_name():
    """
    Function that pops the last name from the list.
    """
    if len(username_list) >= 1:
        print("The name getting popped out is " + username_list[-1])
        username_list.pop()
    else:
        print("No name to pop. Add more name to the list!")


def add_to_username_list(username):
    """
    Function that appends the list with the given username
    """
    username_list.append(username)


can_continue = True

while can_continue:
    print("Pick a choice")
    print("1. Enter a name")
    print("2. Output the list of names")
    print("3. Pop a name from list")
    print("q. Quit")
    user_choice = input("Pick your choice? : ")

    if user_choice == '1':
        add_to_username_list(get_username())
    elif user_choice == '2':
        print_given_name()
    elif user_choice == '3':
        pop_last_name()
    elif user_choice == 'q':
        can_continue = False
    else:
        print("Invalid input. Please pick a value from the list!")
