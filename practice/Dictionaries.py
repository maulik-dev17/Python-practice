# Creating and Accessing Dictionaries:
# 1. Write a Python program to create a dictionary with key-value pairs representing the names of students and their grades. Print the grade of a specific student.

# students = {
#     "Madhavi": 85,
#     "Bhide": 90,
#     "Jethalal": 75,
#     "Daya": 80,
#     "Babita": 75
# }

# print("Babita's grade is:", students["Jethalal"])

# 2. Given a dictionary, write a Python function to add a new key-value pairto it. Also, demonstrate how to update the value of an existing key.Dictionary Methods:

# students = {
#     "Rahul" : 65,
#     "Priya" : 85
# }

# def add_student(dictionary, name, grade):
#     dictionary[name] = grade
# add_student(students, "Amit", 75)
# students["Rahul"] = 95
# print(students)

# 3. Write a Python program to demonstrate the use of the get() method forretrieving values from a dictionary.

# student = {
#     "Name": "Maulik",
#     "Grade": 85,
#     "Age": 22
# }

# print(student.get("Name"))
# print(student.get("Grade"))
# print(student.get("Age"))
# print(student.get("city", "Key not found"))

# 4. Write a Python program to demonstrate the use of the items(), keys(), andvalues() methods to iterate over a dictionary's keys and values.Removing Elements:

# student = {
#     "Name": "Maulik",
#     "Grade": 85,
#     "Age": 22
# }

# print("keys:")
# for key in student.keys():
#     print(key)
    
# print("\nValues:")
# for value in student.values():
#     print(value)
    
# print("\nKey-Value Pairs:")
# for key, value in student.items():
#     print(key, ":", value)

# 5. Write a Python program to remove a specific key-value pair fromdictionary using the pop() method. Also, demonstrate the use of thepopitem() method to remove and return the last inserted key-value pair.Checking Existence of Keys:

# Creating a dictionary
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "grade": 85,
#     "city": "Ahmedabad"
# }

# removed_value = student.pop("age")
# print("Removed value:", removed_value)
# print("Dictionary after pop():", student)

# removed_item = student.popitem()
# print("Removed item:", removed_item)
# print("Dictionary after popitem():", student)

# 6. Write a Python function that checks whether a given key exists in adictionary and returns an appropriate message.

# student = {
#     "name": "Priya",
#     "age": 21,
#     "grade": 90
# }

# def check_key(dictionary, key):
#     if key in dictionary:
#         return "Key exists in the dictionary."
#     else:
#         return "Key does not exist in the dictionary."

# print(check_key(student, "name"))
# print(check_key(student, "city"))

# 7. Intermediate Dictionary OperationsMerging Dictionaries:



# 8. Write a Python program to merge two dictionaries into one. Demonstratehow to handle conflicts if both dictionaries contain the same key.Dictionary Comprehensions:

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 50, 'd': 40, 'e': 60}

# merged_dict = dict1.copy()

# for key, value in dict2.items():
#     if key in merged_dict:
#         print("Conflict found for key:", key)
#         print("Old value:", merged_dict[key])
#         print("New value:", value)

#     merged_dict[key] = value

# print("Merged Dictionary:", merged_dict)

# 9. Write a Python program to create a dictionary using dictionarycomprehension. For example, create a dictionary where the keys arenumbers from 1 to 10 and the values are the squares of the keys.

# squares = {x: x**2 for x in range(1, 11)}
# print("Dictionary of Squares:", squares)