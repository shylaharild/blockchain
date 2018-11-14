# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons_list = [{'name': 'Shyla', 'age': 30,
                'hobbies': ['computers', 'games', 'chess']}, {'name': 'Saranya', 'age': 30,
                'hobbies': ['Shopping', 'Traveling', 'Reading']},  {'name': 'Samriddhi', 'age': 4,
                'hobbies': ['Watching Rhymes', 'Drawing', 'Reading']}]
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
person_name_list = [el['name'] for el in persons_list]
print(person_name_list)
# 3) Use a list comprehension to check whether all persons are older than 20.
person_above_20 = [el['name'] for el in persons_list if el['age'] > 20]
print(person_above_20)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons[:]
print(persons_list)
copied_person_list = persons_list[:]
copied_person_list[0] = {'name': 'Sri', 'age': 30,
                'hobbies': ['computers', 'games', 'chess']}
print(copied_person_list)
# 5) Unpack the persons of the original list into different variables and output these variables.
person_name_list = [el['name'] for el in copied_person_list]
person_age_list = [el['age'] for el in persons_list]
person_hobbies_list = [el['hobbies'] for el in persons_list]
print(person_name_list)
print(person_age_list)
print(person_hobbies_list)