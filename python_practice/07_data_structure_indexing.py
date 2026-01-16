# # Defife a list
# # Data type is string and Data Structure is list
# food = ["Dahi Bhallay", "Biryani", "Daal", "Samosay", "Shami", "palak Paneer"]
# print(food)
# print(food[1])
# print(food[0])
# print(food[-1])
# print(food[-6])
# food[1] = "chicken pulao"  #how to update value
# print(food[1])
# print(food)

# # Tuple
# cordinates = (4.21, 9.29)
# print(cordinates)
# print(cordinates[0])

# # Set
# food_set = {"Dahi Bhallay", "Biryani", "Daal", "Samosay", "Shami", "palak Paneer"}
# print(food_set)
# food_set.add("pakora") #to add element in set 
# print(food_set)


# Dictionary A collection of data stored in key- value pairs like dictionary where you serach for Key word and the get its meaning which is value

# car = {"brand": 'Ford', "model": 'Mustang', "year": 1964}
# print(car)
# print(car['brand'])
# print(car['model'])
# print(car['year'])

# # how to modify a value in dictionary

# car['year'] = 2023
# print(car['year'])
# print(car)

# # table = {
# #     "Feature": ["Ordered", "Mutable", "Allows Duplicates", "Indexing"],
# #     "List": [True, True, True, True],
# #     "Tuple": [True, False, True, True],
# #     "Set": [False, True, False, False],
# #     "Dictionary": [True, True, False, True]
# }



# import pandas as pd

# df = pd.DataFrame({
#     "Feature": ["Ordered", "Mutable", "Allows Duplicates", "Indexing"],
#     "List": [True, True, True, True],
#     "Tuple": [True, False, True, True],
#     "Set": [False, True, False, False],
#     "Dictionary": [True, True, False, True]
# })

# print(df)

i = 1

while i <= 30:
    if i % 2 == 0:
        print(i)
    i = i + 1
