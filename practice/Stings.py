# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# chat gpt Python String Practice
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Level 1: Beginner

# Learn basic string methods.
# 1. Write a program to convert "hello world" into uppercase using upper().

# text = "hello world"
# result = text.upper()
# print(result)

# 2. Convert "PYTHON PROGRAMMING" into lowercase using lower().

# text = "PYTHON PROGRAMMING"
# result = text.lower()
# print(result)

# 3. Convert "python" into "Python" using capitalize().

# text = "python"
# result = text.capitalize()
# print(result)

# 4. Convert "hello world" into "Hello World" using title().

# text = "hello world"
# result = text.title()
# print(result)

# 5. Remove extra spaces from "   Python   " using strip().

# text = "   Python   "
# result = text.strip()
# print(result)

# 6. Count how many times the letter "a" appears in "banana" using count().

# text = "banana"
# result = text.count("a")
# print(result)

# 7. Find the position of "o" in "Hello World" using find().

# text = "Hello World"
# result = text.find("o")
# print(result)

# 8. Check whether "Python" starts with "Py" using startswith().

# text = "Python"
# result = text.startswith("Py")
# print(result)

#    Level 2: Easy

#    Practice searching, replacing and checking strings.
# 9. Check whether "programming" ends with "ing" using endswith().

# text =  "programming"
# result = text.endswith("ing")
# print(result)

# 10. Replace "Java" with "Python" in "I love Java" using replace().

# text = "I love Python"
# result = text.replace("Python", "Java")
# print(result)

# 11. Check whether "12345" contains only digits using isdigit().

# num = "12345"
# result = num.isdigit()
# print(result)

# 12. Check whether "Python" contains only alphabets using isalpha().

# text = "Python"
# result = text.isalpha()
# print(result)

# 13. Check whether "Python123" contains letters and numbers using isalnum().

# text = "Python123"
# result = text.isalnum()
# print(result)

# 14. Split "apple,banana,mango" into a list using split().

# text = "apple, banana, mango"
# result = text.split()
# print(result)

# 15. Join ["I", "love", "Python"] into one string using join().

# text = ["I", "love", "Python"]
# result = " ".join(text)
# print(result)


#     Level 3: Intermediate

#     Combine multiple string methods.
# 16. Write a program to remove spaces from both sides and convert "  hello python  " into uppercase.

# text = "  hello python  "
# result = text.strip().upper()
# print(result)

# 17. Count the number of vowels in "programming" using string methods.

# text = "programming"
# vowels = "aeiou"
# count = sum(1 for char in text if char in vowels)
# print(count)

# 18. Replace all spaces in "Python is easy to learn" with underscores.

# text = "Python is easy to learn"
# result = text.replace(" ", "_")
# print(result)

# 19. Check whether "hello123" is alphanumeric and print the result.

# text = "hello123"
# result = text.isalnum()
# print(result)

# 20. Count how many times the word "Python" appears in "Python is easy. Python is powerful.".

# text = "Python is easy. Python is powerful."
# word = "Python"
# count = text.count(word)
# print(count)

# 21. Write a program to reverse a string after converting it to lowercase.

# text  = "Hello World, Python"
# result = text.lower()[::-1]
# print(result)

# 22. Check whether a given string is a palindrome (e.g. "madam").

# text = input("Enter a string: ")
# text = text.lower()

# if text == text[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")


#     Level 4: Advanced

#     Use logic with multiple string methods.
# 23. Take a sentence from the user and count the number of words using split().

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print("Number of words:", len(words))

# 24. Find the longest word in "Python programming is very interesting".

# sentence = "Python programming is very interesting"
# words = sentence.split()
# longest_word = max(words, key=len)
# print("This is longest_word :",longest_word)

# 25. Take a string from the user and count uppercase and lowercase letters separately.

# string = input("Enter a string :")

# uppercase = 0
# lowercase = 0

# for ch in string:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
# print("uppercase letters: ",uppercase)
# print("lowercase letters: ",lowercase)

# 26. Remove all duplicate characters from "programming" while preserving their original order.

# string = "programming"
# result = ""

# for ch in string:
#     if ch not in result:
#         result += ch
# print("String after removing duplicates:", result)

# 27. Find the first non-repeating character in "swiss".

# string = "swiss"

# for ch in string:
#     if string.count(ch) == 1:
#         print("First non-repeating character:", ch)
#         break


#     Level 5: Expert

#     Challenge yourself with real problem-solving.
# 28. Write a program to find the most frequently occurring character in a given string.

# string = input("Enter a string: ")
# most_frequent = max(string, key = string.count)

# print("Most frequently occurring character:", most_frequent)
# print("Frequency:", string.count(most_frequent))

# 29. Check whether two strings are anagrams (e.g. "listen" and "silent").

# str1 = input("Enter first string :")
# str2 = input("Enter second string :")

# if sorted(str1) == sorted(str2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")

# 30. Take a sentence from the user and convert every word's first letter to uppercase without using title().

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# result = []
# for word in words:
#     result.append(word[0].upper() + word[1:])

# print("Converted sentence:", " ".join(result))
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Kict Python String Practice
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# String Basics:

# 1. Write a Python program to reverse a string without using slicing.

# text = input("Enter you string: ")
# reversed = ""
# for char in text:
#     reversed = char + reversed

# print("reversed string: ", reversed)

# 2. Write a Python program to check if a string is palindrome or not.

# text = input("Enter you string: ")
# reversed = ""
# for char in text:
#     reversed = char + reversed

# if text == reversed:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

# 3. Write a Python program to count the occurrences of a character in a string.

# text = input("Enter a string: ")
# char = input("Enter a character: ")
# count = text.count(char)
# print("Character occurs:", count, "times")

# String Manipulation:
# 1. Write a Python program to count the number of vowels and consonants in a string.

# text = input("Enter a string: ")

# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0

# for char in text.lower():
#     if char in vowels:
#         vowel_count += 1
#     elif char.isalpha():
#         consonant_count += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)

# 2. Write a Python program to find the frequency of each character in a string (ignore case sensitivity).

# text = input("Enter the string: ")
# text = text.lower()
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] =1
# print(frequency)

# 3. Write a Python program to capitalize the first letter of each word in a sentence.

# text = input("Enter a sentence: ")
# result = text.title()
# print(result)

# Substring Operations:
# 1. Write a Python program to check if one string is a rotation of another.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if len(str1) == len(str2) and str2 in (str1 + str1):
#     print("Strings are rotations")
# else:
#     print("Strings are not rotations")

# 2. Write a Python program to find all occurrences of a substring in a given string.

# text = "Python is easy. Python is powerful."
# substring = "Python"
# positions = []
# start = 0

# while True:
#     position = text.find(substring, start)
#     if position == -1:
#         break
#     positions.append(position)
#     start = position + 1

# print("Positions:", positions)

# 3. Write a Python program to remove all leading and trailing whitespace characters from a string.

# text = "    python     "
# result = text.strip()
# print(result)

# String Sorting and Searching:
# 1. Write a Python program to sort words in a sentence alphabetically.

# text = input("Enter a sentence: ")
# words = text.split()
# words.sort(key=str.lower)
# result = " ".join(words)
# print(result)

# 2. Write a Python program to find the longest word in a sentence.

# sentence = "Python programming is very interesting"
# words = sentence.split()
# longest_word = max(words, key=len)
# print("This is longest_word :",longest_word)

# 3. Write a Python program to check if a string contains only digits.

# text = input("Enter a string: ")

# if text.isdigit():
#     print("Contains only digits")
# else:
#     print("Does not contain only digits")

# Advanced String Handling:
# 1. Write a Python program to find the most occurring character in a string.

# text = input("Enter a string: ")

# frequency = {}

# for char in text:
#     if char != " ":
#         frequency[char] = frequency.get(char, 0) + 1

# if frequency:
#     most_common = max(frequency, key=frequency.get)

#     print("Most frequent character:", most_common)
#     print("Frequency:", frequency[most_common])
# else:
#     print("No characters found")

# 2. Write a Python program to check if two strings are anagrams of each other.

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()

# if sorted(str1) == sorted(str2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")

# 3. Write a Python program to find the first non-repeating character in a string.

# text = input("Enter a string: ")

# for char in text:
#     if text.count(char) == 1:
#         print("First non-repeating character:", char)
#         break
# else:
#     print("No non-repeating character found")

# Regular Expressions:
# 1. Write a Python program to validate an email address using regular expressions.

# import re

# email = input("Enter your email: ")

# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# if re.match(pattern, email):
#     print("Valid email")
# else:
#     print("Invalid email")

# 2. Write a Python program to extract numbers from a string using regular expressions.

# import re

# text = "I have 25 apples and 10 mangoes"

# numbers = re.findall(r'\d+', text)

# print(numbers)

# 3. Write a Python program to replace specific patterns in a string using regular expressions.

# import re

# text = "My phone number is 9876543210"

# result = re.sub(r'\d', '*', text)

# print(result)


# Encoding and Decoding:
# 1. Write a Python program to encode a string into base64 format.

# import base64

# text = "Hello Python"

# encoded = base64.b64encode(text.encode())

# print(encoded.decode())

# 2. Write a Python program to decode a base64 encoded string.

# import base64

# encoded = "SGVsbG8gUHl0aG9u"

# decoded = base64.b64decode(encoded).decode()

# print(decoded)
