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

# students = {
#     1: {
#         "name": "Rahul",
#         "age": 20,
#         "marks": 85
#     },
#     2: {
#         "name": "Amit",
#         "age": 21,
#         "marks": 90
#     },
#     3: {
#         "name": "Priya",
#         "age": 19,
#         "marks": 95
#     }
# }

# for roll_no, details in students.items():
#     print("Roll No:", roll_no)
#     print("Name:", details["name"])
#     print("Age:", details["age"])
#     print("Marks:", details["marks"])
#     print("-------------------")

# 27. Write a Python program to find the common keys between two dictionaries.

# dict1 = {
#     "name": "Rahul",
#     "age": 20,
#     "city": "Ahmedabad",
#     "course": "Python"
# }

# dict2 = {
#     "name": "Amit",
#     "age": 22,
#     "salary": 25000,
#     "course": "Java"
# }

# common_keys = dict1.keys() & dict2.keys()

# print("Common keys:", common_keys)

# 28. Student Marks Management System

# Create a dictionary containing five students and their marks.

# Perform the following operations:
# - Display all students and their marks.
# - Add a new student.
# - Update a student's marks.
# - Delete a student.
# - Find the student with the highest marks.
# - Calculate the average marks.

# students = {
#     "Rahul": 85,
#     "Amit": 90,
#     "Priya": 78,
#     "Neha": 95,
#     "Karan": 88
# }

# # 1. Display all students and marks
# print("Student Marks:")

# for name, marks in students.items():
#     print(name, ":", marks)

# # 2. Add a new student
# students["Riya"] = 92

# print("\nAfter Adding Student:")
# print(students)

# # 3. Update student's marks
# students["Rahul"] = 89

# print("\nAfter Updating Marks:")
# print(students)

# # 4. Delete a student
# del students["Karan"]

# print("\nAfter Deleting Student:")
# print(students)

# # 5. Find student with highest marks
# topper = max(students, key=students.get)

# print("\nTopper:", topper)
# print("Highest Marks:", students[topper])

# # 6. Calculate average marks
# average = sum(students.values()) / len(students)

# print("\nAverage Marks:", average)

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

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# print(frequency)

# 30. Shopping Cart System

# Create a dictionary-based shopping cart.

# Perform the following operations:
# - Add products with their prices.
# - Update product prices.
# - Remove products.
# - Display all products and prices.
# - Calculate the total bill.
# - Find the most expensive product.

# cart = {
#     "Laptop": 50000,
#     "Mobile": 20000,
#     "Headphones": 2000,
#     "Keyboard": 1500
# }

# print("Shopping Cart:")

# for product, price in cart.items():
#     print(product, ":", price)

# cart["Mouse"] = 800

# print("\nAfter Adding Product:")
# print(cart)

# cart["Mobile"] = 22000

# print("\nAfter Updating Price:")
# print(cart)

# cart.pop("Keyboard")

# print("\nAfter Removing Product:")
# print(cart)

# total = sum(cart.values())

# print("\nTotal Bill:", total)

# expensive = max(cart, key=cart.get)

# print("\nMost Expensive Product:", expensive)
# print("Price:", cart[expensive])

# This more qutions for learn:

# 1. Create a dictionary named details with the keys name, age, city, and hobbies. Use the same kinds of values shown in the lesson file.

# student = {"name": "Maulik", "age": "23", "city": "Ahemdabad", "hobbies": "movie"}
# print(student)

# 2. Print the complete details dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details)

# 3. Print the value stored under the name key.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details["name"])

# 4. Print the value stored under the city key.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details["city"])

# 5. Print the first item from the hobbies list stored inside the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details["hobbies"][0])

# 6. Print the second item from the hobbies list stored inside the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details["hobbies"][1])

# 7. Print the value stored under the age key.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details["age"])

# 8. Use a for loop to print every key in the details dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# for key in details:
#     print(key)

# 9. Use a for loop to print each key along with its corresponding value in the format key : value.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# for key,value in details.items():
#     print(key, ":" , value)

# 10. Change the age value in the dictionary to 25 and print the updated dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details["age"] = 25

# print(details)

# 11. Change the city value to Surat and print the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details["city"] = "Surat"

# print(details)

# 12. Add a country key with the value India to the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details["country"] = "India"

# print(details)

# 13. Add a course key with a value of your choice to the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"],
#     "country" : "India"
# }

# details["course"] = "Managements"

# print(details)

# 14. Use get() to retrieve the value of the name key.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details.get("name"))

# 15. Use get() to retrieve a key that does not exist, providing an empty string as the default value.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details.get("surname", ""))

# 16. Use get() to retrieve a missing phone key and provide Not available as the default value.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details.get("phone", "Not available"))

# 17. Use setdefault() to add the country key with the value UK if the key does not already exist.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details.setdefault("country","UK")

# print(details)

# 18. Use setdefault() on the city key with the value Surat. Then print the dictionary and observe whether the existing city value changes.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details.setdefault("city", "Surat")

# print(details)

# 19. Store the dictionary's keys in a variable using keys(), then print that variable.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# all_keys = details.keys()

# print(all_keys)
 
# 20. Convert the dictionary's keys into a list and print the list.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# all_keys = list(details.keys())
# print(all_keys)

# 21. Store the dictionary's values in a variable using values(), then print that variable.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# all_values = details.values()

# print(all_values)

# 22. Convert the dictionary's values into a list and print the list.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# all_values = list(details.values())

# print(all_values)

# 23. Check whether the country key exists among the dictionary's keys.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print("country" in details)

# 24. Write an if statement that prints a message when the country key exists in the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "country": "Uk",
#     "hobbies": ["movie", "cricket"]
# }

# if "country" in details:
#     print("country key exists")
# else:
#     print("country key not exists")    

# 25. Check whether the email key exists in the dictionary and print the result.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "country": "Uk",
#     "hobbies": ["movie", "cricket"]
# }

# if "email" in details:
#     print("email key exists")
# else:
#     print("email key not exists") 

# 26. Use pop() to remove the city key from the dictionary. Print the value returned by pop().

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "country": "Uk",
#     "hobbies": ["movie", "cricket"]
# }

# removed_value = details.pop("city")

# print("Removed value:", removed_value)

# 27. Remove the age key using pop() and then print the remaining dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "country": "Uk",
#     "hobbies": ["movie", "cricket"]
# }

# removed_value = details.pop("age")

# print(details)

# 28. Use popitem() to remove one key-value pair from the dictionary and print the returned pair.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "country": "Uk",
#     "hobbies": ["movie", "cricket"]
# }

# removed_item = details.popitem()

# print("Removed item:", removed_item)

# 29. Print the dictionary after using popitem().

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "country": "Uk",
#     "hobbies": ["movie", "cricket"]
# }

# removed_item = details.popitem()

# print("Removed item:", removed_item)

# print(details)

# 30. Make a copy of the details dictionary and store it in a new variable. Print both dictionaries.\
    
# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# new_details = details.copy()

# print("Original Dictionary:", details)
# print("Copied Dictionary:", new_details)

# 31. Change one value in the copied dictionary and print both dictionaries to compare them.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# new_details = details.copy()

# new_details["name"] = "Rahul"

# print("Original Dictionary:", details)
# print("Copied Dictionary:", new_details)

# 32. Use items() to display all key-value pairs in the dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(details.items())

# 33. Convert the result of items() into a list and print it.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# print(list(details.items()))

# 34. Create a second dictionary named details2 containing country and age keys.

# details2 = {
#     "country": "India",
#     "age": "25"
# }

# print(details2)

# 35. Use update() to add the values from details2 to details.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details2 = {
#     "country": "India",
#     "age": "25"
# }

# details.update(details2)

# print(details)

# 36. Create details2 with an age value different from the age value in details. Use update() and print details to observe the result.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details2 = {
#     "age": "55"
# }

# details.update(details2)

# print(details)

# 37. Create a second dictionary with two new keys and use update() to add them to details.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad",
#     "hobbies": ["movie", "cricket"]
# }

# details2 = {
#     "nationality": "Indian",
#        "country" : "India"
# }

# details.update(details2)

# print(details)

# 38. Create a second dictionary containing one existing key and one new key. Use update() and print the final dictionary.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "city": "Ahemdabad"
# }

# details2 = {
#     "age": "25",
#     "country": "India"
# }

# details.update(details2)

# print(details)

# 39. Create a dictionary containing a hobbies list. Access and print the last item in that list using its key and list index.

# details = {
#     "name": "Maulik",
#     "age": "23",
#     "hobbies": ["movie", "cricket", "reading", "music"]
# }

# print(details["hobbies"][-1])

# 40. Create a dictionary of your own with at least four key-value pairs, including one key whose value is a list. Print the dictionary, loop through its keys and values, and display the list's first item.

# details = {
#     "name": "Maulik",
#     "age": 23,
#     "city": "Ahmedabad",
#     "course": "Python",
#     "hobbies": ["movie", "cricket", "music"]
# }

# # Print complete dictionary
# print("Complete Dictionary:")
# print(details)

# # Print all keys and values
# print("\nAll Keys and Values:")

# for key, value in details.items():
#     print(key, ":", value)

# # Print first hobby
# print("\nFirst Hobby:")
# print(details["hobbies"][0])



# simple dictionary making code:
# def convert_to_dict(data):
#     my_dict = {}

#     for item in data.split(","):
#         key, value = item.split(":")
#         my_dict[key] = value

#     return my_dict


# data = input("Enter data: ")

# result = convert_to_dict(data)

# print(result)