#Question 1 : Write A python Program To Find Maximum Between Two Numbers.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if num1 > num2 : 
#     print("Maximum number is:", num1)
# else :
#     print("Maximum number is:", num2)
    
#Question 2 : Write A python Program To Find Maximum Between Three Numbers.
# num1 = float(input("Enter First number: "))
# num2 = float(input("Enter Second number: "))
# num3 = float(input("Enter Third number: "))

# if num1 > num2 and num1 > num3 : 
#     print("Maximun number is: ", num1)
# elif num2 > num1 and num2 > num3 : 
#     print("Maximun number is: ", num2)
# else : 
#     print("Maximun number is : ", num3)

#Question 3 : Write A python Program To Check Whether A Number Is Negative, Positive Or Zero.

# num = float(input("Enter your number: "))

# if  num < 0 :
#     print("number is Nagative: ", num)
# elif num > 0 :
#     print("number is Positive: ", num)
# else : 
#     print("number is Zero: ", num)

#Question 4 : Write A python Program To Check Whether A Number Is Divisible By 5 And 11 Or Not.
# num = float(input("Enter yout number: "))

# if num % 5 == 0 and num % 11 == 0 :
#     print("The number is divisible by both 5 and 11.")
# elif num  % 5 == 0 :
#     print("The number is divisible by 5.") 
# elif num % 11 == 0 :
#     print("The number is divisible by 11.")
# else: 
#     print("The number is not divisible by both 5 and 11.")

#Question 5 : Write A Python Program To Check Whether A Number Is Even Or Odd.    
# num = float(input("Enter your number"))

# if num % 2 == 0: 
#     print("The number is Even.") 
# else:
#     print("The number is Odd.")

#Question 6 : Temperature Check: Write a Python program that takes the temperature as input. If the temperature is above 30 degrees Celsius, print "It's a hot day!" Otherwise, print "It's a cool day."
# num = float(input("Enter your number :"))

# if num > 30 : 
#     print("It's a hot day!")
# else: 
#     print("It's a cold day")

#Question 7 : User Authentication: Create a program that asks the user to enter a username and password. If the username is "admin" and the password is "password123," print "Login successful." Otherwise, print "Invalid credentials."
# userName = (input("Enter your Name :")) 
# password = (input("Enter your Password :"))

# if userName == "admin" and password == "password123" :
#      print ("Login successfull")
# else : 
#     print("Invalid credentials.")

#Question 8 : Write a Python program to check if a given year is a leap year or not.
# year = int(input("Enter a year: "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

#Question 9 : Write a Python program to check if a given character is a vowel or a consonant
# character = input("Enter a character: ")

# if character.lower() in "aeiou":
#     print("Vowel")
# else: 
#     print("Consonant")

#Question 10 : Write a Python program to input the age of a person and determine if they are eligible to vote (18 or older)
# Age =  float(input("Enter the your Age : "))

# if Age >= 18 : 
#     print("Person is eligible to vote")
# else: 
#     print("Person is not eligible to vote")

#Question 11 : Write a Python program to check if a given character is uppercase or lowercase.
# ch = input("Enter a character: ")

# if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     print("The character is uppercase.")
# elif ch in "abcdefghijklmnopqrstuvwxyz":
#     print("The character is lowercase.")
# else:
#     print("The character is neither uppercase nor lowercase.")

#Question 12 :  Write a Python program to input a number representing a day of the week (1 for Monday, 2 for Tuesday, etc.) and print the corresponding day.
# day = int(input("Enter day number (1-7): "))

# days = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }

# if day in days:
#     print("Day:", days[day])
# else:
#     print("Invalid day number")
    
#Question 13 :  Write a Python program to input the month number (1 for January, 2 for February, etc.) and print the number of days in that month (considering leap years)
# month = int(input("Enter month number (1-12): "))
# year = int(input("Enter year: "))

# if month == 2:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print("Number of days: 29")
#     else:
#         print("Number of days: 28")
# elif month in [4, 6, 9, 11]:
#     print("Number of days: 30")
# elif month in [1, 3, 5, 7, 8, 10, 12]:
#     print("Number of days: 31")
# else:
#     print("Invalid month number")

#Question 14 :  Write a Python program to input the marks of four subjects (out of 100) and calculate the average and determine the grade as follows:
# m1 = float(input("Enter marks of subject 1: "))
# m2 = float(input("Enter marks of subject 2: "))
# m3 = float(input("Enter marks of subject 3: "))
# m4 = float(input("Enter marks of subject 4: "))

# average = (m1 + m2 + m3 + m4) / 4

# print("Average:", average)

# if average >= 90:
#     grade = "A"
# elif average >= 80:
#     grade = "B"
# elif average >= 70:
#     grade = "C"
# elif average >= 60:
#     grade = "D"
# elif average >= 50:
#     grade = "E"
# else:
#     grade = "F"

# print("Grade:", grade)

#Question 15 : Write a Python program to input the price of an item and the money given by the customer, then calculate and print the change to be returned.
# price = float(input("Enter price of item: "))
# money = float(input("Enter money given by customer: "))

# if money >= price:
#     change = money - price
#     print("Change to be returned:", change)
# else:
#     print("Insufficient money")

# Intermediate Level:
# 1. Discount Calculator:->Develop a program that asks the user to enter the total amount of a purchase. If the amount is greater than $100, apply a 10% discount and print the final amount. Otherwise, print the original amount. amount = float(input("Enter total purchase amount: "))

# if amount > 100:
#     discount = amount * 0.10
#     final_amount = amount - discount
#     print("Discount:", discount)
#     print("Final amount:", final_amount)
# else:
#     print("Final amount:", amount)

# 2. BMI Calculator:->Write a program that calculates BMI based on user input for weight (in kg) and height (in meters). Classify the BMI as "Underweight," "Normal," "Overweight," or "Obese" using if-else statements.
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))

# bmi = weight / (height ** 2)

# print("BMI:", bmi)

# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")
    
# Advanced Level:

# 1. Ticket Pricing:
# Create a program for a movie ticket booking system. Ask the user for
# their age and determine the ticket price accordingly:
# Children (age < 12): $5
# Adults (12 <= age < 18): $10
# Adults (age >= 18): $15
# age = int(input("Enter your age: "))

# if age < 12:
#     price = 5
# elif age < 18:
#     price = 10
# else:
#     price = 15

# print("Ticket price: $", price)

# Expert Level:

# 1. Airline Reservation System:-> Implement an airline reservation
# system. Ask the user for their destination and the class of service
# (Economy, Business, First). Based on the input, display the ticket price.
# Consider different pricing for different destinations and classes.
# destination = input("Enter destination (Delhi/Mumbai/Dubai): ")
# service_class = input("Enter class (Economy/Business/First): ")

# prices = {
#     "Delhi": {
#         "Economy": 5000,
#         "Business": 10000,
#         "First": 15000
#     },
#     "Mumbai": {
#         "Economy": 6000,
#         "Business": 12000,
#         "First": 18000
#     },
#     "Dubai": {
#         "Economy": 15000,
#         "Business": 30000,
#         "First": 50000
#     }
# }

# if destination in prices and service_class in prices[destination]:
#     price = prices[destination][service_class]
#     print("Ticket price: ₹", price)
# else:
#     print("Invalid destination or class")

# 2. Health Tracker:-> Build a health tracker program that asks the user
# for their daily steps count and sleep hours. Provide feedback based
# on the following conditions:
# If steps < 5000 and sleep < 7 hours: "Improvement needed in
# both steps and sleep."
# If steps < 5000: "Increase your daily steps."
# If sleep < 7 hours: "Ensure you get enough sleep."
# Otherwise: "Great job on maintaining a healthy lifestyle!"
# steps = int(input("Enter your daily steps: "))
# sleep = float(input("Enter your sleep hours: "))

# if steps < 5000 and sleep < 7:
#     print("Improvement needed in both steps and sleep.")
# elif steps < 5000:
#     print("Increase your daily steps.")
# elif sleep < 7:
#     print("Ensure you get enough sleep.")
# else:
#     print("Great job on maintaining a healthy lifestyle!")

## Question 1: Electricity Bill Calculator
# Write a Python program to calculate the electricity bill based on the
# following rates:
#   Units Consumed              Rate per Unit
#   --------------------------- ---------------
#   First 100 units             ₹5
#   Next 100 units (101--200)   ₹7
#   Above 200 units             ₹10
# Display the total bill.

# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 5
# elif units <= 200:
#     bill = (100 * 5) + ((units - 100) * 7)
# else:
#     bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# print("Total Electricity Bill = ₹", bill)


# Question 2: Employee Bonus

# Write a program that asks for:

# -   Employee Name
# -   Years of Experience
# -   Performance Rating (1--5)

# ### Bonus Rules

# -   Experience ≥ 10 years and Rating ≥ 4 → ₹20,000
# -   Experience ≥ 5 years and Rating ≥ 3 → ₹10,000
# -   Experience ≥ 2 years → ₹5,000
# -   Otherwise → No Bonus

# Print the employee name and bonus amount.

# Employee = input("Enter your Employee Name: ")
# Years = float(input("Enter your Years of Experience: "))
# Rating = float(input("Enter your Performance Rating: "))

# if Years >= 10 and Rating >= 4:
#     Bonus = 20000
# elif Years >= 5 and Rating >= 3:
#     Bonus = 10000
# elif Years >= 2:
#     Bonus = 5000
# else:
#     Bonus = 0

# print("Employee Name:", Employee)

# if Bonus > 0:
#     print("Bonus Amount: ₹", Bonus)
# else:
#     print("No Bonus")
    
    
# Question 3: Online Shopping Discount

# A shopping website provides discounts as follows:

# -   Purchase ≥ ₹10,000
#     -   Premium Member → 20% Discount
#     -   Normal Member → 15% Discount
# -   Purchase between ₹5,000 and ₹9,999
#     -   Premium Member → 10% Discount
#     -   Normal Member → 5% Discount
# -   Purchase below ₹5,000
#     -   No Discount

# Take the purchase amount and membership type (Premium or Normal) as
# input and display:

# -   Discount Amount
# -   Final Amount to Pay

# Purchase = float(input("Enter your purchase amount: ₹"))
# Member = input("Enter membership type (Premium/Normal): ")

# if Purchase >= 10000:                 
#     if Member == "Premium":
#         Discount = Purchase * 20 / 100
#     else:
#         Discount = Purchase * 15 / 100

# elif Purchase >= 5000:
#     if Member == "Premium":
#         Discount = Purchase * 10 / 100
#     else:
#         Discount = Purchase * 5 / 100

# else:
#     Discount = 0

# Final_Amount = Purchase - Discount

# print("Discount Amount: ₹", Discount)
# print("Final Amount to Pay: ₹", Final_Amount)

# Question 4: Student Scholarship Eligibility

# A university offers scholarships based on marks and annual family
# income.

# Rules

# -   Marks ≥ 90 and Income \< ₹2,00,000
#     -   100% Scholarship
# -   Marks ≥ 80 and Income \< ₹3,00,000
#     -   75% Scholarship
# -   Marks ≥ 70 and Income \< ₹5,00,000
#     -   50% Scholarship
# -   Marks ≥ 60
#     -   25% Scholarship
# -   Otherwise
#     -   Not Eligible

# Print the scholarship percentage.

# Marks = float(input("Enter your marks: "))
# Income = float(input("Enter your annual family income: ₹"))

# if Marks >= 90 and Income < 200000:
#     Scholarship = 100
# elif Marks >= 80 and Income < 300000:
#     Scholarship = 75   
# elif Marks >= 70 and Income < 500000:
#     Scholarship = 50   
# elif Marks >= 60:
#     Scholarship = 25
# else:
#     Scholarship = 0
    
# if Scholarship > 0:
#     print("Scholarship:", Scholarship, "%")
# else:
#     print("Not Eligible")       