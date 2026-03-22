# import math

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)


# print('Hello World')
# 12 + 3

# x = 1
# y = 2
# unit_price = 1


# student_count = 1000
# print(student_count)

# course = 'Python for Programming'
# print(len(course))    # length of variable
# print((course[0]))    # index of variable
# print((course[-1]))   # negative index starts from opposite side
# print((course[0:3]))  # here index starts from 0,1,2 index gives 'pyt'
# print((course[0:]))   # here if use 0: then python gives us whole string
# print((course[:3]))   # gives ouptput same as [0:3]
# print((course[3:-3]))

# # concatinating
# first = 'Muhammad Usman'
# last = 'Khan'
# full = first + ' ' + last
# print(full)

# # using formatted strings
# first = 'Muhammad Usman'
# last = 'Khan'
# # using formatted strings can put any value in curly braces{{}}
# full = f'{len(first)} {2+2}'
# print(full)

# # Funtions availabe on strings
# course = ' Python for Programming'
# print(course.upper())  # shows course strings in upper case
# print(course.lower())  # shows course strings in Lower case
# print(course.title())  # shows the title
# print(course.strip())  # removes the spaces from begining and end lstrp rstrp
# # Finds the index number in string where pro is available
# print(course.find('Pro'))
# print(course.replace('P', 'j'))  # replaces P in string with j
# print('Pro' in course)  # gives bollean output is it True or False'in'
# print('jython' not in course)

# # Numbers
# x = 1  # integer
# x = 1.1  # float
# x = 1 + 2j  # a+bi    complex numbers

# print(10 + 3)  # addition
# print(10 - 3)  # subtraction
# print(10 * 3)  # multiplication
# print(10 / 3)  # division with floating point
# print(10 // 3)  # division with integer
# print(10 % 3)  # modolus operator 3/10 gives  remainder 1
# print(10 ** 3)  # ** exponenet

# # useful functions with Numbers
# print(round(2.9))
# print(abs(-2.9))

# # importing math function
# math.cos(3)

# # Using input function
# x = input('x: ')
# y = int(x) + 1
# print(f'x: {x}, y: {y}')

# # using bool(x) 0 '' none in booleean context it will be false
# bool(0)

# print((course[3:-3]))

# loops

# from operator import truediv


# temperature = 15
# if temperature > 30:
#     print('it,s warm')
#     print('drink water')
# elif temperature > 20:
#     print('it,s nice')
# else:
#     print('it,s cold')

# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print('eligible for loan')
# else:
#     print('not eligible for loan')


example_list = list(range(1, 6))
print(example_list)

print(example_list[0])


print(example_list[-1])


print(example_list[-2])


print(example_list[:3])


print(example_list[-1:1:-2])

print(example_list[1:2:2])

print(example_list[::2])

print(example_list[::-1])

print(example_list[1::2])

lst = [10, 20, 30, 40, 50, 60]
print(lst[1:5:2])