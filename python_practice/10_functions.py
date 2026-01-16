#  A funtion is block of code which oly runs when it is called 
#  you can pss data known as parameters 
#  can return a data as a result
# defined as'def' keyword

# # lets define a function
# def greet_user():
#     print('Hello, User!')
# greet_user()


# # lets define a function
# def aoa():
#     print('Assalam o Alykum, all the way from london')
# aoa() 
    
    
# ----------------------------------------------------------------------------
#  adding parameters in function

# def aoa(name):
#     print(f'Assalam o alykum, {name}!, kaifa haluk?')
# # aoa('usman')

# # ---------------------------------------------------------------------------
# # defualt parameters
# def aoa(name = 'kiya haal hain'):
#     print(f'Assalam o Alykum, {name}!, chai piyo gay')
# aoa('Rakhshas')
# # ---------------------------------------------------------------------------

# Return Function

# def square(number):
#     return number * number
    
# print(square(9))
    
# Recursion

# def factorial(n):
#     if n ==1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(6))
    
# -------------------------------------------------------------

# sqaure root of (5)
def square(number):
    return number * number

# print(square(5))

# def cube(number):
#     return number ** 3

# print(cube(3))
# print(cube(5))

# def even_or_odd(num):
#     if num % 2 == 0:
#         return 'even number'
#     else:
#         return 'odd number'
    
# print(even_or_odd(5))
# print(even_or_odd(10))
      
# def largest(a,b,c):
#     if a > b and a > c:
#         return ' a is largest'
#     elif b > c and b > a:
#         return 'b is largest'
#     else:
#         return 'c is largest'
    
# print(largest(3, 7, 5))
# print(largest(10, 2, 8))


# def smallest(a,b,c):
#     return min(a,b,c)

# print(smallest(2,6,9))

# def average(a,b,c):
#     return (a + b + c) / 3

# print(average(3, 6, 9))

# Define a factorial returns factorial number


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))
# print(factorial(3))


# def sum_to_n(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_to_n(n-1)
    
# print(sum_to_n(5))
# print(sum_to_n(3))


# Exercise 8: Write a recursive function to count the digits of a number.

# def count_digits_of_n(n):
#     if n < 10:
#         return 1
#     else:
#         return   1 + count_digits_of_n(n // 10)
    
# print(count_digits_of_n(5))
# print(count_digits_of_n(123))
# print(count_digits_of_n(10009))

# lambda function small, anonymous expression written in one line
# x = lambda a: a/2
# print(x(5))


# x = lambda a, b: a * b
# print(x(2,8))

# Write a lambda function that returns the cube of a number.

# cube = lambda n: n ** 3
# print(cube(3))
# print(cube(5))

# Exercise 2: Write a lambda function that returns the bigger of two numbers

# bigger_num = lambda a, b: 'a is bigger' if a > b else 'b is bigger'
# print(bigger_num(10,7))
# print(bigger_num(4,9))

# Exercise 3: Write a lambda function to check if a number is positive, negative, or zero
check = lambda n: 'positive' if n > 0 else ('negative' if n < 0 else 'zero')

print(check(5))
print(check(-3))
print(check(0))