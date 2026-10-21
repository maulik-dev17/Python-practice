# 1.  Write a Python function to find the maximum between two numbers.
# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(maximum(12, 20))

# 2.  Write a Python function to find the maximum between three numbers.
# def maximum(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print(maximum(10, 25, 15))

# 3.  Write a Python function to check whether a number is negative, positive, or zero.
# def check_number(n):
#     if n > 0:
#         print("Positive")
#     elif n < 0:
#         print("Negative")
#     else:
#         print("Zero")

# check_number(0)

# 4.  Write a Python function to check whether a number is divisible by 5 and 11 or not.
# def divisible(n):
#     if n % 5 == 0 and n % 11 == 0:
#         print("Divisible by 5 and 11")
#     else:
#         print("Not divisible by 5 and 11")

# divisible(5)

# 5.  Write a Python function to check whether a number is even or odd.
# def even_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# even_odd(8)

# 6.  Write a Python function to check whether a character is an alphabet or not.
# def check_alphabet(ch):
#     if ch.isalpha() and len(ch) == 1:
#         print("Alphabet")
#     else:
#         print("Not an alphabet")

# check_alphabet("s")


# 7.  Write a Python function to input any alphabet and check whether it is a vowel or consonant.
# def vowel_consonant(ch):
#     if len(ch) == 1 and ch.isalpha():
#         if ch.lower() in "aeiou":
#             print("Vowel")
#         else:
#             print("Consonant")
#     else:
#         print("Invalid input")
        
# vowel_consonant("10")

# 8.  Write a Python function to input any character and check whether it is an alphabet, digit, or special character.
# def check_character(ch):
#     if len(ch) != 1:
#         print("Enter a single character")
#     elif ch.isalpha():
#         print("Alphabet")
#     elif ch.isdigit():
#         print("Digit")
#     else:
#         print("Special character")

# check_character("a")

# 9.  Write a Python function to check whether a character is uppercase or lowercase alphabet.
# def check_case(ch):
#     if len(ch) == 1 and  ch.isalpha():
#         if ch.isupper():
#             print("Uppercase")
#         else:
#             print("Lowercase")
#     else:
#         print("Not an alphabet")

# check_case("1")

# 10. Write a Python function to input a week number and print the weekday.
# def weekday(n):
#     days = ["Monday", "Tuesday", "Wednesday", "Thusday", "Friday", "Saturday", "Sunday"]
    
#     if 1 <= n <= 7:
#         print(days[n - 1])
#     else:
#         print("Invalid week number")

# weekday(4)

# 11. Write a Python function to input a month number and print the number of days in that month.
# def month_days(n):
#     if n in [1, 3, 5, 7, 8, 10, 12]:
#         print("31 Days")
#     elif n in [4, 6, 9, 11]:
#         print("30 Days")
#     elif n == 2:
#         print("28 or 29 days")
#     else:
#         print("Invalid month number")

# month_days(11)

# 12. Write a Python function to calculate profit or loss.
# def profit_loss(cost_price, selling_price):
#     if selling_price > cost_price:
#         print("Profit =", selling_price - cost_price)
#     elif selling_price < cost_price:
#         print("Loss =", cost_price - selling_price)
#     else:
#         print("No profit, No loss")

# profit_loss(1000, 800)

# 13. Write a Python function to input marks of five subjects (Physics, Chemistry,
# Biology, Mathematics, and Computer), calculate percentage, and grade
# according to the following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

# def calculate_grade ():
#     Physics = float(input("Enter Physics marks: "))
#     Chemistry = float(input("Enter Chemistry marks: "))
#     Biology = float(input("Enter Biology marks: "))
#     Mathematics = float(input("Enter Mathematics marks: "))
#     Computer = float(input("Enter Computer marks: "))

#     total = Physics + Chemistry + Biology + Mathematics + Computer
#     percentage = total / 5
    
#     print("Percentage =", percentage, "%")
    
#     if percentage >= 90:
#         print("Grade A")
#     elif percentage >= 80:
#         print("Grade B")    
#     elif percentage >= 70:
#         print("Grade C")    
#     elif percentage >= 60:
#         print("Grade D")    
#     elif percentage >= 40:
#         print("Grade E")
#     else:
#         print("Grade F")    

# calculate_grade()

# 14. Write a Python function to input the basic salary of an employee and
# calculate its gross salary according to the following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 78%
# Write a Python function to count the total number of notes in a given
# amount.

# def gross_salary():
#     basic = float(input("Enter basic salary: "))

#     if basic <= 10000:
#         hra = basic * 0.20
#         da = basic * 0.80
#     elif basic <= 20000:
#         hra = basic * 0.25
#         da = basic * 0.90
#     else:
#         hra = basic * 0.30
#         da = basic * 0.78

#     gross = basic + hra + da

#     print("HRA =", hra)
#     print("DA =", da)
#     print("Gross Salary =", gross)

# gross_salary()

# def count_notes():
#     amount = int(input("Enter amount: "))

#     denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
#     total_notes = 0

#     for note in denominations:
#         count = amount // note
#         if count > 0:
#             print(note, "=", count, "notes")

#         total_notes += count
#         amount = amount % note

#     print("Total number of notes =", total_notes)

# count_notes()

# 15. Write a Python program to find a cube of any number using a function.
# def cube(n):
#     return n ** 3

# num = int(input("Enter a number: "))
# print("Cube = ",cube(num))

# 16. Write a Python program to the find diameter, circumference, and area of the circle using functions.
# def diameter(r):
#     return 2 * r

# def circumference(r):
#     return 2 * 3.15 * r *r

# def area(r):
#     return 3.15 * r * r

# radius = float(input("Enter radius: "))

# print("Diameter =", diameter(radius))
# print("Circumference =", circumference(radius))
# print("Area =", area(radius))

# 17. Write a Python program to find the maximum and minimum between two numbers using functions.
# def maximum (a, b):
#     return max(a, b)

# def minimum(a, b):
#     return min(a, b)

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("Maximum =", maximum(x, y))
# print("Minimum =", minimum(x, y))

# 18. Write a Python program to check whether a number is even or odd using functions.
# def checkNumber(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# num = int(input("Enter your number: "))
# print(checkNumber(num))    

# 19. Write a Python program to check whether a number is prime, Armstrong, or perfect number using functions.
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# def is_armstrong(n):
#     digits = str(n)
#     total = sum(int(d) ** len(digits) for d in digits)
#     return n >= 0 and total == n


# def is_perfect(n):
#     if n < 2:
#         return False
#     total = sum(i for i in range(1, n) if n % i == 0)
#     return total == n


# num = int(input("Enter a number: "))

# print("Prime:", is_prime(num))
# print("Armstrong:", is_armstrong(num))
# print("Perfect:", is_perfect(num))

# 20. Write a Python program to find all prime numbers between given intervals using functions.
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % 1 == 0:
#             return False
#     return True

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# print("Prime numbers:")
# for n in range(start, end + 1):
#     if is_prime(n):
#         print(n, end=" ")
    
# 21. Write a Python program to print all strong numbers between given intervals using functions.
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact

# def is_strong(n):
#     total = 0
#     for d in str(n):
#         total += factorial(int(d))
#     return n >= 0 and total == n

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# print("Strong numbers:")
# for n in range(start, end + 1):
#     if is_strong(n):
#         print(n, end=" ")

# 22. Write a Python program to print all Armstrong numbers between given intervals using functions.
# def is_armstrong(n):
#     digits = str(n)
#     total = sum(int(d)** len(digits) for d in digits)
#     return n >= 0 and total == n

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# print("Armstrong numbers:")
# for n in range(start, end + 1):
#     if is_armstrong(n):
#         print(n, end=" ")

# 23. Write a Python program to print all perfect numbers between given intervals using functions.
# def is_perfect(n):
#     if n < 2:
#         return False
#     total = sum(i for i in range(1, n) if n % i == 0)
#     return total == n

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# print("Perfect numbers:")
# for n in range(start, end + 1):
#     if is_perfect(n):
#         print(n, end=" ")

# 24. Write a Python program to find the power of any number using recursion.
# def power(a, b):
#     if b == 0:
#         return 1
#     return a * power(a, b - 1)

# num = int(input("Enter base: "))
# exp = int(input("Enter exponent (non-negative): "))

# if exp < 0:
#     print("Please enter a non-negative exponent.")
# else:
#     print("Power =", power(num, exp))

# 25. Write a Python program to print all natural numbers between 1 to n using recursion.
# def natural(n):
#     if n == 0:
#         return
#     natural(n - 1)
#     print(n, end=" ")

# num = int(input("Enter n: "))

# if num >= 1:
#     natural(num)

# 26. Write a Python program to print all even or odd numbers in given range using recursion.
# def print_numbers(start, end, choice):
#     if start > end:
#         return

#     if start % 2 == choice:
#         print(start, end=" ")

#     print_numbers(start + 1, end, choice)

# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))

# choice = input("Enter even or odd: ").lower()

# if choice == "even":
#     print_numbers(start, end, 0)
# elif choice == "odd":
#     print_numbers(start, end, 1)
# else:
#     print("Invalid choice")        

# 27. Write a Python program to find sum of all natural numbers between 1 to n using recursion.
# def natural_sum(n):
#     if n == 0:
#         return 0
#     return n + natural_sum(n - 1)

# num =  int(input("Enter n: "))

# if num >= 0:
#     print("Sum =", natural_sum(num))
# else:
#     print("Please enter a non-negative number.")

# 28. Write a Python program to find the sum of all even or odd numbers in a given range using recursion.
# def sum_numbers(start, end, choise):
#     if start > end:
#         return 0
    
#     if start % 2 == choise:
#         return start + sum_numbers(start + 1, end, choise)
#     else:
#         return sum_numbers(start + 1, end, choise)
    
# start = int(input("Enter starting number: "))
# end = int(input("Enter ending number: "))
# choice = input("Enter even or odd: ").lower()

# if choice == "even":
#     print("Sum =", sum_numbers(start, end, 0))
# elif choice == "odd":
#     print("Sum =", sum_numbers(start, end, 1))
# else:
#     print("Invalid choice")

# 29. Write a Python program to find the reverse of any number using recursion.
# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# num = int(input("Enter a number: "))
# sign = -1 if num < 0 else 1

# print("Reverse =", sign * reverse_number(abs(num)))

# 30. Write a Python program to check whether a number is a palindrome or not using recursion.
# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# num = int(input("Enter a number: "))

# if num >= 0 and num == reverse_number(num):
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")

# 31. Write a Python program to find the sum of digits of a given number using recursion.
# def sum_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits(n // 10)

# num = int(input("Enter a number: "))
# print("Sum of digits = ", sum_digits(abs(num)))

# 32. Write a Python program to find the factorial of any number using recursion.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n -1)

# num = int(input("Enter a non-negative number: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers")
# else: 
#     print("Factorial =", factorial(num))

# 33. Write a Python program to generate nth Fibonacci term using recursion.
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input("Enter term number (starting from 0): "))

# if num < 0:
#     print("Enter a non-negative number")
# else:
#     print("Fibonacci term =", fibonacci(num))

# 34. Write a Python program to find the GCD (HCF) of two numbers using recursion.
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("GCD (HCF) =", gcd(abs(x), abs(y)))

# 35. Write a Python program to find the LCM of two numbers using recursion.
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# def lcm(a, b):
#     if a == 0 or b == 0:
#         return 0
#     return abs(a * b) // gcd(abs(a), abs(b))

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("LCM =", lcm(x, y))

# 36. Write a Python program to display all array elements using recursion.
# def display(arr, index):
#     if index == len(arr):
#         return
#     print(arr[index], end=" ")
#     display(arr, index + 1)

# arr = list(map(int, input("Enter array elements: ").split()))

# print("Array elements:")
# display(arr, 0)

# 37. Write a Python program to find the sum of elements of an array using recursion.
# def array_sum(arr, index):
#     if index == len(arr):
#         return 0
#     return arr[index] + array_sum(arr, index + 1)

# arr = list(map(int, input("Enter array elements: ").split()))

# print("Sum of array elements =", array_sum(arr, 0))

# 38. Write a Python program to find maximum and minimum elements in array using  recursion.
# def find_max(arr, index):
#     if index == len(arr) - 1:
#         return arr[index]
#     return max(arr[index], find_max(arr, index + 1))

# def find_min(arr, index):
#     if index == len(arr) - 1:
#         return arr[index]
#     return min(arr[index], find_min(arr, index + 1))

# arr = list(map(int, input("Enter array elements: ").split()))

# if len(arr) == 0:
#     print("Array is empty")
# else:
#     print("Maximum =", find_max(arr, 0))
#     print("Minimum =", find_min(arr, 0))