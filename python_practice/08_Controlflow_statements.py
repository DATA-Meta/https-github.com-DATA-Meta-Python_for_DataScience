# conditional statements
# >,>,==,!=

# x = 0
# if x > 0:
#     print('x is positive')
# elif x < 0:
#     print('x is negative') 
# else:
#     print('x is zero')       

#  for loop
# menu = ["Dahi Bhallay", "Biryani", "Daal", "Samosay", "Shami", "palak Paneer"]

# # print(menu[0]) inorder to avoid writing too much code used below for loop
# # print(menu[0])

# for food in menu:
#     print(food)


#  while Loop

# i = 1
# while i < 1:
#     print(i)
#     i = i+1


# control flows Break, Continue, pass

# for letters in "PYTHON":
#     if letters == "H":
#         break
#     print(letters)
    
# for letters in "PYTHON":
#     if letters == "H":
#         continue
#     print(letters)

# for letters in "PYTHON":
#     if letters == "H":
#         pass
#     print(letters)

# MASTER PRACTICE SHEET: Loops + Conditions + Operators
# Below are 20 exercises that will make you strong in:
# if, elif, else
# for loops
# while loops
# comparison operators: >, <, ==, !=, <=, >=
# control flow: break, continue
# Each exercise is small but powerful.

#-----------------------------------------------------------------------------
# SECTION 1: IF‑STATEMENT PRACTICE (5 exercises)
# 1. Check if a number is positive, negative, or zero

# num = 0
# if num > 0:
#     print("number is positive")
# elif num < 0:
#     print("Number is Negative")
# else:
#     print('Number is zero')
#---------------------------------------------------------------------------------
# # 2. Check if a person is eligible to vote
# # Condition:
# # age >= 18 → eligible
# # else → not eligible

# age = 18

# if age >=18:
#     print("Eligible to vote")
# else:
#     print("nopt eligible to vote")

#------------------------------------------------------------------------------

# 3. Compare two numbers
# Given two numbers:
# print which one is greater
# print if they are equal

# x = 10
# y = 2

# if x > y:
#     print('x is greater than y')
# elif x < y:
#     print('y is bigger than x')
# else:
#     print('both are equal')

#------------------------------------------------------------------------------

# 4. Check if a number is even or odd
# Use:
# num % 2 == 0 → even
# else → odd

# x = -10

# if x % 2 == 0:
#     print('x is even number')
# else:
#     print('x is odd number')

#-------------------------------------------------------------------------------

# 5. Grade system
# Based on marks:
# A: marks >= 90
# B: marks >= 80
# C: marks >= 70
# D: marks >= 60
# F: marks < 60

# marks =45

# if marks >= 90:
#     print('excellent grade')
# elif marks >= 80:
#     print('very good grade')
# elif marks >= 70:
#     print(' good grade')
# elif marks >= 60:
#     print('fair grade')
# else:
#     print('fail')
    
# -----------------------------------------------------------------------------

# ✅ SECTION 2: FOR‑LOOP PRACTICE (5 Exercises)
# 6. Print numbers from 1 to 20
# Use a for loop with range(1, 21).

# for i in range(1,21):
#     print(i)

# ------------------------------------------------------------------------------

#Print only even numbers from 1 to 50

# for i in range(1,50):
#     if i % 2 == 0:
#         print(i)
 
# -----------------------------------------------------------------------------

#8. Loop through a list of fruits and print each one. 
# ✅ Goal:  
# Create a list of fruits and use a for loop to print each fruit.

# fruits = ['apple',' banana', 'mango', 'orange']
# for fruit in fruits:
#     print(fruit)

#------------------------------------------------------------------------------

#9. Print the sum of numbers from 1 to 100
# ✅ Goal:  
# Use a for loop to add numbers from 1 to 100.
# total = 0
# for i in range(1,101):
#     total = total + i
# print(total)

# -----------------------------------------------------------------------------

# 10. Print all numbers divisible by 5 between 1 and 100
# ✅ Use a for loop
# ✅ Check num % 5 == 0

# for num in range(1,101):
#     if num % 5 == 0:
#         print(num)

# -----------------------------------------------------------------------------

# 11. Print numbers from 1 to 10 using a while loop
# Start: i = 1
# Loop while i <= 10
# Increment inside the loop

# i = 1
# while i <= 10:
#     print(i)
#     i = i +1

#------------------------------------------------------------------------------

# 12. Print numbers from 10 down to 1

# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

# ------------------------------------------------------------------------------

#Keep asking the user for a number until they enter 0

# num = 5
# while num != 0:
#     print('number is', num)
#     num = int(input('Enter a number: '))

#------------------------------------------------------------------------------


# 14. Print the sum of numbers from 1 to 50 using a while loop
# ✅ Goal
# Use a while loop to add numbers from 1 to 50.
 
# i = 1
# total = 0
# while i <= 50:
#     total = total + i
#     i = i +1
# print(total)

# 15. Print all even numbers between 1 and 30 using a while loop
# i = 1

# while i <= 30:
#     if i % 2 == 0:
#         print(i)
# i = i +1        

i = 1
while i <= 30:
    if i % 2 == 0:
        print(i)
i = i + 1        