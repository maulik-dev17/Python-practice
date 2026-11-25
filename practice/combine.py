# PYTHON STRING AND LIST PRACTICE QUESTIONS
# Level: Beginner to Intermediate
# Total Questions: 30
# Solutions: Not included

# SECTION 1: BASIC STRING OPERATIONS

# 1. Given name = "Aarav Sharma", print the string and its length.

# name = "Aarav Sharma"
# print(name)
# print(len(name))

# 2. Given name = "Priya Deshmukh", print the first character, last character, and character at index 4.

# name = "Priya Deshmukh"
# print("First character: ",name[0])
# print("Last character: ",name[-1])
# print("Character at index 4: ",name[4])

# 3. Given name = "rohan patel", convert it into uppercase, lowercase, title case, and capitalized form.

# name = "rohan patel"

# print("Uppercase:", name.upper())
# print("Lowercase:", name.lower())
# print("Title case:", name.title())
# print("Capitalized:", name.capitalize())

# 4. Given name = "Ananya Verma", check whether "Ananya" and "Verma" are present in the string.

# name = "Ananya Verma"
# print("Ananya" in name)
# print("Verma" in name)

# 5. Given email = "rahul@gmail.com", check whether it starts with "rahul" and ends with ".com".

# email = "rahul@gmail.com"
# print("Starts with rahul:", email.startswith("rahul"))
# print("Ends with .com:", email.endswith(".com"))

# 6. Given name = "Vikram Joshi", display the name centered within 30 characters using "-" and "*".

# name = "Vikram Joshi"
# print(name.center(30, "-"))
# print(name.center(30, "*"))

# 7. Given text = "Amit123", check whether it contains only alphabetic characters, only digits, or a combination of letters and digits.

# text = "Amit123"

# if text.isalpha():
#     print("Only alphabets")
# elif text.isdigit():
#     print("Only digits")
# elif text.isalnum():
#     print("Combination of letters and digits")
# else:
#     print("Contains special characters or spaces")

# 8. Given name = "Kavita Mehta", find the index of "a" and the index of "Mehta".

# name = "Kavita Mehta"
# print("Find the index of 'a': ", name.find("a"))
# print("Find the index of 'Mehta': ", name.find("Mehta"))

# 9. Given name = "neha gupta", check whether it is in title case.

# name = "neha gupta"
# print(name.istitle())

# 10. Given name = "siddhiiii", replace the first three occurrences of "i" with "z".

# name = "siddhiiii"
# result = name.replace("i", "z", 3)
# print(result)

# SECTION 2: STRING AND LIST COMBINED QUESTIONS

# 11. Given students = "Aarav Priya Kunal Sneha", split the string into a list, add "Ishita" at the end, and join the names using commas.

# students = "Aarav Priya Kunal Sneha"
# name = students.split()
# name.append("Ishita")
# result = ",".join(name)
# print(result)

# 12. Given cities = "Surat Mumbai Pune Ahmedabad Jaipur", convert the string into a list, sort the cities alphabetically, and join them using " - ".

# cities = "Surat Mumbai Pune Ahmedabad Jaipur"
# city_list = cities.split()
# city_list.sort()
# result = " - ".join(city_list)
# print(result)

# 13. Given text = "Python Java Python C++ Java Python", convert the string into a list and count the occurrences of "Python" and "Java".

# text = "Python Java Python C++ Java Python"
# words = text.split()
# print("Python:", words.count("Python"))
# print("Java:", words.count("Java"))

# 14. Given students = "Rahul Pooja Amit Neha", insert "Sanjay" at index 2 and display the updated list and joined string.

# students = "Rahul Pooja Amit Neha"
# names = students.split()
# names.insert(2, "Sanjay")
# print(names)
# print(" ".join(names))

# 15. Given fruits = "mango apple banana orange", remove "apple" from the list and join the remaining fruits using commas.

# fruits = "mango apple banana orange"
# fruit_list = fruits.split()
# fruit_list.remove("apple")
# result = ",".join(fruit_list)
# print(result)

# 16. Given items = "pen pencil eraser sharpener", remove the last item using pop() and display the removed item and remaining list.

# items = "pen pencil eraser sharpener"
# item_list = items.split()
# removed_item = item_list.pop()
# print("Removed item:", removed_item)
# print("Remaining list:", item_list)

# 17. Given names = "rohan priya amit rohan neha priya", remove one occurrence of "rohan", sort the list, and display the result.

# names = "rohan priya amit rohan neha priya"
# name_list = names.split()
# name_list.remove("rohan")
# name_list.sort()
# print(name_list)

# 18. Given numbers = "50 10 40 20 30", convert the values into integers, sort them in ascending order, and print the result.

# numbers = "50 10 40 20 30"
# numbers_list = numbers.split()
# numbers_list = [int(i) for i in numbers_list]
# numbers_list.sort()
# print(numbers_list)

# 19. Given students = "Aarav Isha Aarav Kabir Isha Aarav", count how many times each student's name appears.

# students = "Aarav Isha Aarav Kabir Isha Aarav"
# students_list = students.split()
# for name in set(students_list):
#     print(name, ":", students_list.count(name))

# 20. Given words = "coding learning programming", split the string, reverse the list using a list method, and join the words into a new sentence.

# words = "coding learning programming"
# word_list = words.split()
# word_list.reverse()
# result = " ".join(word_list)
# print(result)

# SECTION 3: REAL-WORLD STRING PROBLEM-SOLVING

# 21. USERNAME GENERATOR
# Given full_name = "Aarav Rajesh Sharma", generate the username "aarav_rajesh_sharma" using string and list methods.

# full_name = "Aarav Rajesh Sharma"
# username = full_name.split()
# resutl = "_".join(username)
# print(resutl)

# 22. EMAIL FILTERING
# From the given list, display email addresses that end with "@gmail.com" and have a non-empty username.

# emails = [
#     "aarav@gmail.com",
#     "priya@yahoo.com",
#     "kabir@gmail.com",
#     "invalid-email",
#     "@gmail.com"
# ]

# for email in emails:
#     if email.endswith("@gmail.com") and email.split("@")[0] != "":
#         print(email)

# 23. DUPLICATE WORD REMOVAL
# Given sentence = "rahul likes cricket and rahul likes football", create a list of unique words while preserving their original order, then join them into a sentence.

# sentence = "rahul likes cricket and rahul likes football"
# words = sentence.split()
# unique_words = []
# for word in words:
#     if word not in unique_words:
#         unique_words.append(word)

# result = " ".join(unique_words)

# print("Duplicate values: ",unique_words)
# print(result)

# 24. LONGEST WORD FINDER
# Given sentence = "Shreya enjoys learning Python programming", find the longest word using a loop and list operations.

# 25. WORD LENGTH ANALYSIS
# Given sentence = "Amit studies computer science", create a list containing the length of each word.

# 26. CHARACTER FREQUENCY
# Given text = "maharashtra", count the occurrences of every unique character using string and list operations.

# 27. REMOVE UNWANTED WORDS
# Given sentence = "Riya is very smart and Riya is very hardworking", remove "very" and "and" from the word list and create a new sentence.

# 28. SORT WORDS BY LENGTH
# Given sentence = "Ishita likes learning Python programming", arrange the words from shortest to longest.

# 29. WORD REPLACEMENT
# Given sentence = "Rohan likes Java. Rohan practices Java.", replace "Java" with "Python", split the result into a list, reverse the list, and join it again.

# 30. STUDENT NAME PROCESSING
# Clean the names, remove duplicates, sort them alphabetically, and display the final names separated by commas.

# students = "  Aarav, Priya, Kabir, Aarav, Sneha, Priya  "


# PRACTICE INSTRUCTION
# Try solving the questions using the concepts from your Python string file. For combined problems, use split(), join(), strip(), replace(), and relevant list methods such as append(), extend(), insert(), remove(), pop(), sort(), reverse(), count(), and index().
