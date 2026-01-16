# name = input() #User input
# # print(name) #output

# print("Hello", name)

# name = input("Enter your name:") #User input
#  print(name) #output

# print("Hello", name, ", or sunao?")

# # Program to calculate age of person A and pertson B
# person_A_name = input("what is your name:")
# person_A_age  = input("enter your age:")

# person_B_name = input("what is your name:")
# person_B_age  = input("enter your age:")

# if person_A_age > person_B_age:
#     print(person_A_name, "is older than", person_B_name)
# else:
#      print(person_A_name, "is younger than", person_B_name)
     
#BMI calculator ask age , weight, and height

# person_name = input("what is your name:")
# weight= int( input("what is your weight:"))
# height = int(input("enter your height:"))
# height_in_inches = float(input("Enter your height in inches: "))

# # Convert inches to meters
# height_in_meters = height_in_inches * 0.0254

# bmi = weight/height ** 2

# print("your BMI is: ")

person_name = input("What is your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))








