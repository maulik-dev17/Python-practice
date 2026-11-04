# 🟢 PART 1: LISTS (15 Questions)
# These questions will help you understand creating lists, accessing elements, modifying lists, and using list methods.

# Beginner Level (1–5)
# Q1. Create a List
# furits = ["Bananas", "Apple", "Oranges", "Pineapple"]
# print(furits)

# Create a list containing 5 different fruits and print the list.

# Q2. Access Elements

# Create this list:
# numbers = [10, 20, 30, 40, 50]
# print(numbers[0], numbers[2], numbers[-1])

# Print:
# - First element
# - Third element
# - Last element
# Q3. Change Elements

# Create this list:
# colors = ["red", "blue", "green"]

# colors[1] = "yellow"
# print(colors)

# Change "blue" to "yellow" and print the updated list.

# Q4. Add Elements

# Create a list of 3 animals.
# - Add "Tiger" at the end.
# - Add "Lion" at the beginning.
# - Print the updated list.

# Animals = ["Dog", "Cat", "Elephant"]
# Animals.append("Tiger")
# Animals.insert(0,"Lion")

# print(Animals)

# Q5. Remove Elements

# Create this list:
# names = ["Amit", "Rahul", "Priya", "Karan"]

# names.remove("Priya")
# print(names)

# Remove "Priya" and print the updated list.
# Intermediate Level (6–10)
# Q6. Find List Length

# numbers = [10, 20, 30, 40, 50, 60, 70]

# print(len(numbers))

# Create a list of 7 numbers and print how many elements are in the list.

# Q7. List Slicing

# Given:
# numbers = [10, 20, 30, 40, 50, 60, 70]

# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[2:6])
# print(numbers[::-1])

# Print:
# - First 3 elements.
# - Last 3 elements.
# - Elements from index 2 to 5.
# - Reverse the list using slicing.
# Q8. Sum of Elements

# Given:
# numbers = [10, 20, 30, 40, 50]

# print(sum(numbers))

# Calculate and print the sum of all numbers.

# Q9. Find the Largest Number

# Given:
# numbers = [45, 12, 89, 34, 67, 99, 23]

# print(max(numbers))

# Find the largest number in the list.

# Q10. Count Occurrences

# Given:
# numbers = [10, 20, 10, 30, 10, 40, 20]

# print(numbers.count(10))

# Count how many times 10 appears in the list.
# Challenge Level (11–15)
# Q11. Separate Even and Odd Numbers

# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
        
# print("Even :",even)
# print("Odd: ",odd)

# Create two separate lists:
# - One containing even numbers.
# - One containing odd numbers.
# Q12. Remove Duplicates

# Given:
# numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]


# Create a new list without duplicate elements.

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print(unique)

# Try to maintain the original order.

# Q13. Sort a List

# Given:
# numbers = [45, 12, 89, 34, 67, 23]

# numbers.sort()
# print("Ascending:", numbers)

# numbers.sort(reverse=True)
# print("Descending:", numbers)

# Sort the list:
# - In ascending order.
# - In descending order.
# Q14. Find the Second Largest Number

# Given:
# numbers = [10, 50, 30, 90, 70, 90]


# unique = list(set(numbers))
# unique.sort()

# print("Second largest:", unique[-2])

# Find the second-largest unique number.

# Q15. List Reversal Challenge

# Given:
# numbers = [1, 2, 3, 4, 5]

# reversed_list = []

# for num in numbers:
#     reversed_list.insert(0, num)

# print(reversed_list)

# Reverse the list without using:
# - reverse()
# - Slicing ([::-1])

# Try solving it using a loop.

# 🟡 PART 2: TUPLES (15 Questions)
# These questions will help you understand tuple creation, indexing, slicing, unpacking, and tuple operations.
# Beginner Level (1–5)
# Q16. Create a Tuple
# Create a tuple containing 5 different programming languages and print it.

# languages = ("Python", "Java", "C++", "JavaScript", "PHP")
# print(languages)

# Q17. Access Elements

# Given:
# languages = ("Python", "Java", "C++", "JavaScript", "PHP")

# print(languages[0])
# print(languages[2])
# print(languages[-1])

# Print:
# - First element.
# - Third element.
# - Last element.
# Q18. Tuple Length

# Given:
# numbers = (10, 20, 30, 40, 50, 60)

# print(len(numbers))

# Find the length of the tuple.

# Q19. Tuple Slicing

# Given:
# numbers = (10, 20, 30, 40, 50, 60, 70)

# print(numbers[:3])
# print(numbers[-3:])
# print(numbers[::-1])

# Print:
# - First 3 elements.
# - Last 3 elements.
# - Reverse the tuple using slicing.
# Q20. Count Elements

# Given:
# numbers = (10, 20, 10, 30, 10, 40, 20)

# print(numbers.count(10))

# Count how many times 10 appears.
# Intermediate Level (6–10)
# Q21. Find an Element

# Given:
# fruits = ("apple", "banana", "mango", "orange")

# print(fruits.index("mango"))

# Find the index position of "mango".

# Q22. Check an Element

# Given:
# colors = ("red", "green", "blue", "yellow")

# print("green" in colors)

# Check whether "green" exists in the tuple.

# Print True or False.

# Q23. Tuple Concatenation

# Create two tuples:
# a = (1, 2, 3) 
# b = (4, 5, 6)

# result = a + b
# print(result)

# Combine them into one tuple.

# Q24. Tuple Repetition

# Given:
# numbers = (1, 2, 3)

# result = numbers * 3
# print(result)

# Repeat this tuple 3 times and print the result.

# Q25. Tuple Unpacking

# Given:
# student = ("Rahul", 20, "Python")

# name, age, course = student

# print(name)
# print(age)
# print(course)

# Unpack the tuple into three variables:
# - name
# - age
# - course
# Print all three variables.
# Challenge Level (11–15)
# Q26. Swap Two Variables

# Create two variables:
# a = 10b = 20

# a, b = b, a

# print("a =", a)
# print("b =", b)

# Swap their values using tuple unpacking.

# Q27. Find Maximum and Minimum

# Given:
# numbers = (45, 12, 89, 34, 67, 99, 23)

# print("Maximum :",max(numbers))
# print("Minimum :",min(numbers))

# Find the maximum and minimum values.

# Q28. Convert List to Tuple

# Given:
# numbers = [10, 20, 30, 40, 50]

# result = tuple(numbers)
# print(result)

# Convert this list into a tuple.

# Q29. Nested Tuple

# Given:
# students = (    ("Amit", 85),    ("Rahul", 90),    ("Priya", 95))

# print(students[1][1])
# print(students[2][1])
# print(students[0][0])

# Print:
# - Rahul's marks.
# - Priya's marks.
# - Amit's name.
# Q30. Single Element Tuple

# Create a tuple containing only one element: "Python".

# language = ("Python",)

# print(type(language))

# Print its type and make sure the output is <class 'tuple'>.
# 🔵 PART 3: RANGES (15 Questions)
# These questions will help you understand range(), start, stop, step, loops, and number sequences.
# Beginner Level (1–5)
# Q31. Basic Range

# Use range() to print numbers from 0 to 9 using a loop.

# Q32. Start and Stop

# Use range() to print numbers from 1 to 20.

# Q33. Even Numbers

# Use range() to print all even numbers from 2 to 20.

# Q34. Odd Numbers

# Use range() to print all odd numbers from 1 to 19.

# Q35. Reverse Range

# Use range() to print numbers from 10 down to 1.
# Intermediate Level (6–10)
# Q36. Multiplication Table

# Take a number from the user and print its multiplication table from 1 to 10 using range().

# Q37. Sum of Numbers

# Use range() and a loop to calculate the sum of numbers from 1 to 100.

# Q38. Multiples of 5

# Use range() to print all multiples of 5 between 5 and 100.

# Q39. Range with Step

# What will be the output of this code?
# for i in range(2, 21, 3):    print(i)


# Try to understand how the step value works.

# Q40. Convert Range to List

# Convert this range into a list and print it:
# numbers = range(1, 11)


# Challenge Level (11–15)
# Q41. Countdown

# Use range() to print:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Start!

# Q42. Sum of Even Numbers

# Use range() to calculate the sum of all even numbers between 1 and 100.

# Q43. Find Divisible Numbers

# Use range() and a loop to print all numbers between 1 and 100 that are divisible by both 3 and 5.

# Q44. Factorial

# Take a number from the user and calculate its factorial using range().

# Example:
# Enter number: 5
# Factorial: 120

# Q45. Number Pattern

# Use range() and nested loops to print this pattern:
# 1
# 12
# 123
# 1234
# 12345

