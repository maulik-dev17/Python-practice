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

# student = {
#     'name': 'Rahul',
#     'age': 20,
#     'course': 'Python'
# }

# print("Original Dictionary:", student)
# print("Keys:", student.keys())
# print("Values:", student.values())
# student['age'] = 21
# print("After Updating:", student)
# student['city'] = 'Ahmedabad'
# print("After Adding:", student)
# del student['course']
# print("After Deleting:", student)
# print("name" in student)

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

# 1. Create a dictionary containing a student's name, age, course, and city. Print the dictionary.

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# print(students)

# 2. Write a Python program to access the value of a given key in a dictionary.

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# print(students[0]["name"])
# print(students[0]["age"])
# print(students[0]["course"])
# print(students[0]["city"])

# print('------------------------------------------------------')

# print(students[1]["name"])
# print(students[1]["age"])
# print(students[1]["course"])
# print(students[1]["city"])

# print('------------------------------------------------------')

# print(students[2]["name"])
# print(students[2]["age"])
# print(students[2]["course"])
# print(students[2]["city"])

# 3. Write a Python program to add a new key-value pair to an existing dictionary.

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# students[0]["state"] = "Gujarat"
# students[1]["state"] = "Gujarat"
# students[2]["state"] = "Maharashtra"
# print(students)

# 4. Write a Python program to update the value of an existing key in a dictionary.

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# students[1]["age"] = 21
# print(students)

# 5. Write a Python program to delete a key from a dictionary using the del keyword.

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# del students[0]["course"]
# del students[1]["course"]
# del students[2]["course"]

# print(students)

# 6. Write a Python program to find the length of a dictionary using len().

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# print(len(students))

# 7. Write a Python program to check whether a particular key exists in a dictionary.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# if "age" in students:
#     print("Key exists")
# else:
#     print("Key does not exist")
    
# if "name" in students:
#     print("Key exists")
# else:
#     print("Key does not exist")

# if "course" in students:
#     print("Key exists")
# else:
#     print("Key does not exist")

# if "state" in students:
#     print("Key exists")
# else:
    # print("Key does not exist")
    
# 8. Write a Python program to print all keys and values of a dictionary separately.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# print("keys :")
# for key in students.keys():
#     print(key)
    
# print("----------------------------------")
    
# print("values :")
# for value in students.values():
#     print(value)

# 9. Write a Python program to use the get() method to access a key. If the key does not exist, return a default message.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# print(students.get("name", "Key not found"))
# print(students.get("age", "Key not found"))
# print(students.get("course", "Key not found"))
# print(students.get("state", "Key not found"))

# 10. Write a Python program to use the pop() method to remove a particular key from a dictionary.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# print(students.pop("course"))
# print(students)

# 11. Write a Python program to use the popitem() method to remove the last inserted item.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# print(students.popitem())
# print(students)

# 12. Write a Python program to copy one dictionary into another using the copy() method.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}
# print(students.copy())
# print(students.popitem())

# 13. Write a Python program to remove all elements from a dictionary using clear().

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}
# students.clear()
# print(students)

# 14. Write a Python program to iterate through a dictionary using a for loop and print each key-value pair.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# for key, value in students.items():
#     print(key, ":" ,value)

# 15. Write a Python program to count how many key-value pairs are present in a dictionary.

# students = {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"}

# count = len(students)
# print("Total key-value pairs:",count)

# 16. Write a Python program to find the sum of all values in a dictionary.

# students_grades = {
#     "Gujarati": 85,
#     "Math": 75,
#     "Sicence": 95,
#     "Social Sicence": 90,
#     "English": 80,
# }

# total = sum(students_grades.values())
# print("sum of all the grades:" ,total)

# 17. Write a Python program to find the maximum and minimum values in a dictionary.

# students_grades = {
#     "Gujarati": 85,
#     "Math": 75,
#     "Sicence": 95,
#     "Social Sicence": 90,
#     "English": 80,
# }

# maximun = max(students_grades.values())
# minimun = min(students_grades.values())

# print("Maximum numbers :", maximun)
# print("Manimum numbers :", minimun)

# 18. Write a Python program to count the number of times each character appears in a given string using a dictionary.

# test = "programming"

# char_count = {}

# for char in test:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# print(char_count)

# 19. Write a Python program to merge two dictionaries. If the same key exists, add their values instead of replacing them.

# student1 = {"gujarati": 85, "Math": 75, "Sicence": 95, "Social_Sicence": 90, "English": 80}
# student2 = {"gujarati": 90, "Math": 80, "Sicence": 85, "Social_Sicence": 95, "English": 75}

# result = student1.copy()

# for key, value in student2.items():
#     result[key] = (result.get(key, 0) + value) / 2

# print(result)

# 20. Write a Python program to create a dictionary containing numbers from 1 to 20 as keys and their cubes as values.

# cude = {}

# for i in range(1, 21):
#     cude[i] = i ** 3
# print(cude)

# 21. Write a Python program to find the key associated with the maximum value in a dictionary.

# students_grades = {
#     "Gujarati": 85,
#     "Math": 75,
#     "Sicence": 95,
#     "Social Sicence": 90,
#     "English": 80,
# } 

# max = max(students_grades, key = students_grades.get)
# min = min(students_grades, key = students_grades.get)

# print(max, "has the maximum value of", students_grades[max])
# print(min, "has the minimum value of", students_grades[min])

# 22. Write a Python program to reverse a dictionary (swap keys and values).

# students = [
#     {"name": "Hetal", "age": 21, "course": "Marketing", "city": "Ahmedabad"},
#     {"name": "Huma", "age": 20, "course": "Human research", "city": "Baroda"},
#     {"name": "Manu", "age": 21, "course": "Coding", "city": "Mumbai"},
# ]

# reversed = {}
# for student in students:
#     for key, value in student.items():
#         reversed[value] = key
# print(reversed)
# -----------------------------------or---------------------------------------------
 
# reversed_dict = {}

# for student in students:
#     for key, value in student.items():
#         if key not in reversed_dict:
#             reversed_dict[key] = []

#         reversed_dict[key].append(value)

# print(reversed_dict)
  
# 23. Write a Python program to sort a dictionary by its values in ascending order.

# wiht lambda function
# students_grades = {
#     "Gujarati": 85,
#     "Math": 75,
#     "Sicence": 95,
#     "Social Sicence": 90,
#     "English": 80,
# }

# sorted_grades = dict(
#     sorted(students_grades.items(), key=lambda item: item[1])
# )

# print(sorted_grades)

# ------------------------------------or---------------------------------------------

# without lambda function
# students_grades = {
#     "Gujarati": 85,
#     "Math": 75,
#     "Science": 95,
#     "Social Science": 90,
#     "English": 80,
# }

# def get_value(item):
#     return item[1]

# sorted_grades = dict(
#     sorted(students_grades.items(), key=get_value)
# )

# print(sorted_grades)

# 24. Write a Python program to remove duplicate values from a dictionary.

# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30,
#     "e": 20
# }

# result = {}

# for key, value in data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)

# 25. Write a Python program to combine three dictionaries into one dictionary.

# dict1 = {"a": 10, "b": 20}
# dict2 = {"c": 30, "d": 40}
# dict3 = {"e": 50, "f": 60}

# result = {}

# result.update(dict1)
# result.update(dict2)
# result.update(dict3)

# print(result)

# 26. Write a Python program to create a nested dictionary containing the details of three students (name, age, marks). Display the details of each student.

# 27. Write a Python program to find the common keys between two dictionaries.

# 28. Student Marks Management System

# Create a dictionary containing five students and their marks.

# Perform the following operations:
# - Display all students and their marks.
# - Add a new student.
# - Update a student's marks.
# - Delete a student.
# - Find the student with the highest marks.
# - Calculate the average marks.
# 29. Word Frequency Counter

# Write a Python program that accepts a sentence from the user and counts how many times each word appears.

# Example:
# Input: apple banana apple mango banana apple

# Output:
# {
#     'apple': 3,
#     'banana': 2,
#     'mango': 1
# }

# 30. Shopping Cart System

# Create a dictionary-based shopping cart.

# Perform the following operations:
# - Add products with their prices.
# - Update product prices.
# - Remove products.
# - Display all products and prices.
# - Calculate the total bill.
# - Find the most expensive product.