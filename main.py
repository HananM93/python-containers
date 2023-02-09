# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['Ashley', 'Bri','Lacie','Andi']
print(students[1])
print(students[3])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the studentslist.
# Use a for loop to print out the string "food goes here is a good food".

foods = 'burger','steak','pasta','sushi'

for food in foods:
    print(f"{food} is a good food")


# Exercise 3
# Using a for loop, print just the last two food strings from foods.

for food in range(-2,0):
    print(foods[food])



# Exercise 4
# Create a dictionary named home_town containing the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city': 'Saint Paul',
    'state': 'Minnesota',
    'pouplation': '307,193'
}

print(f"I grew up in {home_town['city']}, {home_town['state']} - population: {home_town['pouplation']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
    # "city = Arcadia"
	# "state = California"
	# "population = 58000"

for key,val in home_town.items():
    print(f"{key} = {val}")