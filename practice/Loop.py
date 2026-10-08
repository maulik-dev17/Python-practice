# 1. Write a Python program to print all natural numbers from 1 to n. - using while loop
# n = int(input("Enter Number: "))

# i = 1
# while i <= n:
#     print(i)
#     i += 1

# 2. Write a Python program to print all natural numbers in reverse (from n to 1). - using while loop
# n = int(input("Enter Number: "))

# i = n
# while i >= 1:
#     print(i)
#     i -= 1

# 3. Write a Python program to print all alphabets from a to z. - using while loop
# i = ord("a")

# while i <= ord("z"):
#       print(chr(i))
#       i += 1

# 4. Write a Python program to print all even numbers between 1 to 100. - using while loop
# i = 2

# while i <= 100:
#     print(i)
#     i += 2

# 5. Write a Python program to print all odd number between 1 to 100.
# i = 1

# while i <= 100:
#     print(i)
#     i += 2

# 6. Write a Python program to find sum of all natural numbers between 1 to n.
# n = int(input("Enter n: "))

# i = 1
# sum = 0

# while i <= n:
#     sum += i
#     i += 1

# print("Sum =", sum)

# 7. Write a Python program to find sum of all even numbers between 1 to n.
# n = int(input("Enter n: "))

# i = 2
# sum = 0

# while i <= n:
#     sum += i
#     i += 2

# print("Sum of even numbers =", sum)

# 8. Write a Python program to find sum of all odd numbers between 1 to n.
# n = int(input("Enter n: "))

# i = 1
# sum = 0

# while i <= n:
#     sum += i
#     i += 2

# print("Sum of odd numbers =", sum)

# 9. Write a Python program to print multiplication table of any number.
# n = int(input("Enter a number: "))

# i = 1

# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1

# 10. Write a Python program to count number of digits in a number.
# n = int(input("Enter a number: "))

# n = abs(n)
# count = 0

# if n == 0:
#     count = 1
# else:
#     while n > 0:
#         count += 1
#         n //= 10

# print("Number of digits =", count)

# 11. Write a Python program to find first and last digit of a number.
# n = int(input("Enter a number: "))

# n = abs(n)

# last_digit = n % 10

# while n >= 10:
#     n //= 10

# first_digit = n

# print("First digit =", first_digit)
# print("Last digit =", last_digit)

# 12. Write a Python program to find sum of first and last digit of a number.
# n = int(input("Enter a number: "))

# n = abs(n)

# last_digit = n % 10

# while n >= 10:
#     n //= 10

# first_digit = n

# sum = first_digit + last_digit

# print("Sum of first and last digit =", sum)

# 14. Write a Python program to calculate sum of digits of a number.
# n = int(input("Enter a number: "))

# n = abs(n)
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10
    
# print("Sum of digits=", sum)

# 15. Write a Python program to calculate product of digits of a number.
# n = int(input("Enter a number: "))

# n = abs(n)
# product = 1

# while n > 0:
#     digit = n % 10
#     product *= digit
#     n //= 10

# print("Product of digits =", product)

# 16. Write a Python program to enter a number and print its reverse.
# n = int(input("Enter a number: "))

# n = abs(n)
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# print("Reverse =", reverse)

# 17. Write a Python program to check whether a number is palindrome or not.
# n = int(input("Enter a number: "))

# original = n
# n = abs(n)
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# if abs(original) == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 18. Write a Python program to find frequency of each digit in a given integer.
# n = int(input("Enter a number: "))

# n = abs(n)

# for i in range(10):
#     count = 0
#     temp = n

#     while temp > 0:
#         digit = temp % 10

#         if digit == i:
#             count += 1

#         temp //= 10

#     if count > 0:
#         print(i, "=", count)

# 19. Write a Python program to enter a number and print it in words.
# n = int(input("Enter a number: "))

# words = [
#     "Zero", "One", "Two", "Three", "Four",
#     "Five", "Six", "Seven", "Eight", "Nine"
# ]

# n = abs(n)

# if n == 0:
#     print("Zero")
# else:
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n //= 10

#     while reverse > 0:
#         digit = reverse % 10
#         print(words[digit], end=" ")
#         reverse //= 10

# 20. Write a Python program to print all ASCII character with their values.
# for i in range(0, 128):
#     print(i, "=", chr(i))

# 21. Write a Python program to find power of a number using for loop.
# base = int(input("Enter base: "))
# power = int(input("Enter power: "))

# result = 1

# for i in range(power):
#     result *= base

# print("Answer =", result)

# 22. Write a Python program to find all factors of a number.
# n = int(input("Enter a number: "))

# print("Factors are:")

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

# 23. Write a Python program to calculate factorial of a number.
# n = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print("Factorial =", factorial)

# 24. Write a Python program to find HCF (GCD) of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0 :
#     a, b = b, a % b

# print("HCF =", a)

# 25. Write a Python program to find LCM of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# while y != 0:
#     x, y = y, x % y
    
# hcf = x 
# lcm = (a * b) // hcf

# print("LCM = ", lcm)

# 26. Write a Python program to check whether a number is Prime number or not.
# n = int(input("Enter a number: "))

# count = 0
# i = 1

# while i <= n:
#     if n % i == 0:
#         count += 1
#     i += 1

# if count == 2:
#     print("Prime number")
# else:
#     print("Not a prime number")

# 27. Write a Python program to print all Prime numbers between 1 to n.
# n = int(input("Enter Number: "))

# num = 2

# while num <= n:
#     count = 0
#     i = 1
    
#     while i <= num:
#         if num % 1 == 0:
#             count += 1
#         i += 1
        
#     if count == 2:
#         print(num)
    
#     num += 1 

# 28. Write a Python program to find sum of all prime numbers between 1 to n.
# n = int(input("Enter n: "))

# num = 2
# sum = 0

# while num <= n:
#     count = 0
#     i = 1

#     while i <= num:
#         if num % i == 0:
#             count += 1
#         i += 1

#     if count == 2:
#         sum += num

#     num += 1

# print("Sum of prime numbers =", sum)

# 29. Write a Python program to find all prime factors of a number.
# n = int(input("Enter a number: "))

# i = 2

# print("Prime factors are: ")

# while i <= n:
#     if n % i == 0:
#         count = 0
#         j = 1
        
#         while j <= i:
#             if i % j == 0:
#                 count += 1
#             j += 1
        
#         if count == 2:
#             print(i)
            
#     i += 1        

# 30. Write a Python program to check whether a number is Armstrong number or not.
# n = int(input("Enter a number: "))

# original = n
# temp = n
# count = 0

# while temp > 0:
#     count += 1
#     temp //= 10

# temp = n
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** count
#     temp //= 10

# if sum == original:
#     print("Armstrong number")
# else: 
#     print("Not an Armstrong number")    

# 31. Write a Python program to print all Armstrong numbers between 1 to n.
n = int(input("Enter n: "))

num = 1

while num <= n:
    temp = num
    count = 0

    while temp > 0:
        count += 1
        temp //= 10

    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** count
        temp //= 10

    if sum == num:
        print(num)

    num += 1

# 32. Write a Python program to check whether a number is Perfect number or not.
n = int(input("Enter a number: "))

sum = 0
i = 1

while i < n:
    if n % i == 0:
        sum += i
    i += 1

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")

# 33. Write a Python program to print all Perfect numbers between 1 to n.
n = int(input("Enter n: "))

num = 1

while num <= n:
    sum = 0
    i = 1

    while i < num:
        if num % i == 0:
            sum += i
        i += 1

    if sum == num:
        print(num)

    num += 1

# 34. Write a Python program to check whether a number is Strong number or not.
n = int(input("Enter a number: "))

original = n
sum = 0

while n > 0:
    digit = n % 10

    factorial = 1
    i = 1

    while i <= digit:
        factorial *= i
        i += 1

    sum += factorial
    n //= 10

if sum == original:
    print("Strong number")
else:
    print("Not a strong number")

# 35. Write a Python program to print all Strong numbers between 1 to n.
n = int(input("Enter n: "))

num = 1

while num <= n:
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10

        factorial = 1
        i = 1

        while i <= digit:
            factorial *= i
            i += 1

        sum += factorial
        temp //= 10

    if sum == num:
        print(num)

    num += 1