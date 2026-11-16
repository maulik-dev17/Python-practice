# PYTHON LIST - 50 PRACTICE QUESTIONS

# 1. Create a list containing 5 integers and print the complete list.
# numbers = [10, 20, 30, 40, 50]
# print(numbers)

# 2. Create a list containing an integer, float, string, and boolean. Print the list.
# my_list = [1, 2, 3, "Pythone", "JavaScript", True, False]
# print(my_list)

# 3. Given numbers = [10, 20, 30, 40, 50], print the first element, third element, and last element.
# numbers = [10, 20, 30, 40, 50]

# print(numbers[0])
# print(numbers[2])
# print(numbers[-1])

# 4. Given numbers = [10, 20, 30, 40, 50], change the third element to 100 and print the list.
# numbers = [10, 20, 30, 40, 50]

# numbers[2] = 100

# print(numbers)

# 5. Create a list of 5 names and use a for loop to print every name.

# names = ["Maulik", "Python", "Dhurvi", "Dharana", "Java"]
# for name in names:
#     print(name)

# 6. Create a list using list(range(1, 11)) and print all the values.

# numbers = list(range(1, 11))
# print(numbers)

# 7. Create a list containing numbers from 10 to 20 using range().

# numbers = list(range(10, 21))
# print(numbers)

# 8. Given numbers = [5, 10, 15, 20, 25], print the length of the list.

# numbers = [5, 10, 15, 20, 25]
# print(len(numbers))

# 9. Given a list of names, print the last element using len() instead of directly using a negative index.

# names = ["Dhruvi", "Mansi", "Tamanna", "Mahi"]
# print(names[len(names) - 1])

# 10. Given names = ["Dhruvi", "Mansi", "Tamanna"], add "Mahi" at the end using append().

# names = ["Dhruvi", "Mansi", "Tamanna"]
# names.append("Mahi")
# print(names)

# 11. Create a list of numbers and append three new numbers one by one.

# numbers = [10, 20, 30, 40]
# numbers.append(50)
# numbers.append(60)
# numbers.append(70)
# print(numbers)

# 12. Given names = ["Dhruvi", "Mansi", "Tamanna", "Mahi"], remove the element at index 1 using pop() and print both the updated list and removed value.

# names = ["Dhruvi", "Mansi", "Tamanna", "Mahi"]
# removed_value = names.pop(1)
# print("Updated list:", names)
# print("Removed value:", removed_value)

# 13. Create a list of 5 numbers, remove the last element using pop(), and print the removed value.

# numbers = [10, 20, 30, 40, 50, 60]
# numbers.pop()
# print("Updated list:", numbers)

# 14. Given names = ["Dhruvi", "Mansi", "Tamanna"], insert "Mahi" at index 1.

# names = ["Dhruvi", "Mansi", "Tamanna"]
# names.insert(1, "Mahi")
# print(names)

# 15. Create a list of numbers and insert 100 at the beginning of the list.

# numbers = [10, 20, 30, 40, 50, 60]
# numbers.insert(0, 100)
# print(numbers)

# 16. Given a = [1, 2, 3] and b = [4, 5, 6], combine b into a using extend().

# a = [1, 2, 3]
# b = [4, 5, 6]

# a.extend(b)
# print(a)

# 17. What is the difference between append() and extend()? Demonstrate the difference using two lists.

# a = [1, 2, 3]
# b = [1, 2, 3]

# a.append([4, 5, 6])
# b.extend([4, 5, 6])

# print("Append:", a)
# print("Extend:", b)

# append() adds an entire object as one element.
# extend() adds each element individually.

# 18. Given names = ["Raj", "Mahi"], add ["Dhruvi", "Mansi"] using append() and observe the result.

# names = ["Raj", "Mahi"]
# names.append(["Dhruvi", "Mansi"])
# print(names)

# 19. Given the same lists, use extend() instead of append() and observe the difference.

# names = ["Raj", "Mahi"]
# names.extend(["Dhruvi", "Mansi"])
# print(names)

# 20. Create a list of names, make a copy using copy(), add a new name to the original list, and print both lists.

# names = ["Dhruvi", "Mansi", "Mahi"]
# new_names = names.copy()
# names.append("Tamanna")

# print("Original list:", names)
# print("Copied list:", new_names)

# 21. Explain the difference between b = a and b = a.copy(). Demonstrate it with a list.

# a = [10, 20, 30]
# b = a
# c = a.copy()

# a.append(40)

# print("a:", a)
# print("b:", b)
# print("c:", c)

# b = a means both variables refer to the same list.
# c = a.copy() creates a separate shallow copy.

# 22. Given a = [10, 20, 30] and b = a.copy(), change an element in a and check whether b changes.

# a = [10, 20, 30]
# b = a.copy()

# a[0] = 100

# print("a:", a)
# print("b:", b)

# 23. Given names = ["Dhruvi", "Mansi", "Mahi", "Sunita"], reverse the list using reverse().

# names = ["Dhruvi", "Mansi", "Mahi", "Sunita"]
# names.reverse()
# print(names)

# 24. Given a list of numbers, sort the list in ascending order using sort().

# numbers = [50, 10, 40, 20, 30]
# numbers.sort()
# print(numbers)

# 25. Given a list of numbers, sort the list in descending order using sort(reverse=True).

# numbers = [50, 10, 40, 20, 30]
# numbers.sort(reverse=True)
# print(numbers)

# 26. Given names = ["Mansi", "Dhruvi", "Mansi", "Mahi", "Mansi"], count how many times "Mansi" occurs.

# names = ["Mansi", "Dhruvi", "Mansi", "Mahi", "Mansi"]
# print(names.count("Mansi"))

# 27. Given a list of numbers, count how many times 10 occurs.

# numbers = [10, 20, 10, 30, 10, 40, 50]
# print(numbers.count(10))

# 28. Create a list, use clear() to remove all elements, and print the resulting list.

# numbers = [10, 20, 10, 30, 10, 40, 50]
# numbers.clear()
# print(numbers)

# 29. Given a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], print elements from index 0 to 5 using slicing.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[0:6])

# 30. Using the same list, print elements from index 3 to 7.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[3:8])

# 31. Using the same list, print the first 5 elements using slicing without specifying the starting index.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[:5])

# 32. Using the same list, print all elements starting from index 4 using slicing.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[4:])

# 33. What happens when you use a[4:100] on a list containing only 10 elements? Demonstrate it.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[4:100])

# 34. Using a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], print the elements from index 8 down to index 4 in reverse order.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[8:4:-1])

# 35. Using negative indexing, print the last element, second-last element, and sixth-last element.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(a[-1])
# print(a[-2])
# print(a[-6])

# 36. Using slicing with negative indexes, print the last 5 elements of a list.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[-5:])

# 37. Reverse an entire list using slicing [::-1].

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::-1])

# 38. Print every second element from a list using slicing.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[::2])

# 39. Given a list of numbers from 1 to 20, create a new list containing only even numbers using list comprehension.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_numbers = [i for i in numbers if i % 2 == 0]
# print(even_numbers)

# 40. Given a list of numbers from 1 to 20, create a new list containing only odd numbers using list comprehension.

# numbers = list(range(1, 21))
# odd_numbers = [i for i in numbers if i % 2 != 0]
# print(odd_numbers)

# 41. Using list comprehension, create a list containing the squares of numbers from 1 to 10.

# squares = [i ** 2 for i in range(1, 11)]
# print(squares)

# 42. Given numbers = [3, 4, 5, 6, 2, 7, 8, 9, 1, 2, 5, 6, 7, 2, 3, 5], create a new list containing only numbers greater than 5.

# numbers = [3, 4, 5, 6, 2, 7, 8, 9, 1, 2, 5, 6, 7, 2, 3, 5]
# new_numbers = [i for i in numbers if i > 5]
# print(new_numbers)

# 43. Given a list of numbers, create a new list containing the cubes of only even numbers using list comprehension.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_cubes = [i ** 3 for i in numbers if i % 2 == 0]
# print(even_cubes)

# 44. Create the following 2D list:
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     Print the complete list.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix)

# 45. Given a 2D list, use a for loop to print each inner list separately.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     print(row)

# 46. Given a 2D list, use nested for loops to print every individual element.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for element in row:
#         print(element)

# 47. Given matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]], print the value 50 using list indexing.

# matrix = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# print(matrix[1][1])

# 48. Ask the user how many numbers they want to enter. Take all numbers using a loop, store them in a list, and print the final list.

# n = int(input("How many numbers do you want to enter? "))
# numbers = []
# for i in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)
# print("Final list:", numbers)

# 49. Take 5 numbers from the user, store them in a list, and then create another list containing only the even numbers using list comprehension.

# numbers = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# even_numbers = [i for i in numbers if i % 2 == 0]

# print("Original list:", numbers)
# print("Even numbers:", even_numbers)

# 50. Ask the user to enter their name and age, then display the information using an f-string. Also create a list containing the user's name, age, and another value, and print the list.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# print(f"My name is {name} and my age is {age}")

# my_list = [name, age, "Python"]

# print(my_list)
