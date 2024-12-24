# DAY 2
# Exercise 1: Calculation
# milk = 2.5
# bread = 3.80
# eggs = 2

# cost = milk + bread + float(eggs)
# print(f"Your totla is: ${cost}.")
# print("\n")

# Exercise 2: String Manipulation
# opening_phrase = "Welcome to "    # Setting a opening phrase 
# user = input("What is the store name: ") # get the name from the user via input command

# print(opening_phrase + user + "!.") # Concatenate opening phrase and the input entered by the user
# print("\n") # Add a new line to the screen               

# Exercise 3: Common Errors
# milk = "3"
# bread = 2.5
# total = float(milk) + bread
# print(f"The total cost is: ${total}")
# ---------- End of Day 2 ----------

#Day 3
# List: Flexible and let you add, remove and change data
# Tuple: Great for locking in data

# List Practice Exercises 
# ---------- 1. List Manipulation ----------
movies = ["Resident Evil Series", "Toy Story", "Space Jam", "Taken Series", "007 Series", "Mission Impossible"]
# Add a new movie to the end of the list:
# Method to use: .append()
movies.append("Demon Slayer") #Adding Demon Slayer to the movie list
print(movies)

# Remove the second movie from the list:
# Method to use: .remove()
movies.remove("Toy Story") #Removing Toy Story, the second movie, from the list
print(movies)

# ---------- 2. Indexing and Slicing ----------
# Using a list of numbers, retrieve the last two items without using negative indices
numbers = [10, 20, 30, 40, 50]
expected_output = numbers[3:]  #Slicing from the item in index 3 to the end
print(expected_output)

# ---------- 3. Inserting Items ----------
colors = ["red", "blue", 'green']
# Insert yellow at the second and purple at the end of the list
# .insert() does not return any value, so will print none if assigned to a new variable that has the inserted item to the list you want to modify
colors.insert(1, "yellow")
print(colors)
colors.insert(5, "purple")
print(colors)

# Tuple Practice Exercises
# ---------- 1. Creating and Indexing a Tuple ----------
dimension = (10, 5, 15)
print(dimension[1])

# ---------- 2. Slicing a Tuple ----------
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(numbers[2:6]) #Slicing from index 2 to index 6, but not including index 6

# ---------- 3. Concatenating Tuples ---------
fruits = ("apple", "banana")
vegetables = ("carrot", "lettuce")
#combine the above tuples into a new tuple 
groceries = fruits + vegetables
print(groceries)

# Dictionary Practice Exercises 
# ---------- Creating and Accessing Values ----------
book = {"title": "1984", "author": "George Orwell", "year": 1949} # Create a dictionary 
print(book["author"])  # Access and print the value for the key author

# ---------- Adding and Updating Entries ----------
profile = {} # Create an empty dictionary
profile["name"] = "Alice"  # Adding name and assigning value to it to the dictionary
profile["age"] = 30 # Adding age and assigning value to it to the dictionary
profile["city"] = "Paris" # Adding city and assigning value to it to the dictionary
print(profile)
profile["city"] = "London" # Update the value for existing key, city,  in the dictionary
print(profile)

# ---------- Removing and Retrieving Keys and Values ----------
student = {"name": "Emma", "grade": "A", "subject": "Math"}

# removing the subject key using pop and retrieve the remaining keys and values separately
student.pop("subject")
print(student)
print(student.keys())  # Retrieve all the keys stored in the dictionary
print(student.values()) # Retrieve all the values stored in the dictionary

# Sets Practice Exercises
# Note: Sets do not allow duplicate values and are unordered(No Specific order or indexing)
# ADDING ELEMENTS: 
#    - .add()
# REMOVING ELEMENTS: .remove() (raises an error if the item is not found)
#    - .remove() (raises an error if the item is not found)
#    - .discard() (doesn’t raise an error if the item isn’t found)
# SET OPERATIONS:
#    - .union() Combines two sets, keeping only unique items.
#    - .intersection() Finds common items between two sets.
#    - .difference() Shows items in one set but not in the other.

# ---------- Adding and Removing Elements ----------
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
fruits.add("banana")  # Sets will not add this because it exists in the set already, no duplicates allowed
print(fruits)
fruits.discard("banana")
print(fruits) # Removing banana from the set alternatively if the item is in the set, using .remove() can also work

# ---------- Union and Intersection ----------
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # Combines the two sets and only allow non duplicate items to be added, and stores to a new set
print(set_a.intersection(set_b)) # Finds the common items, that are duplicates between the two sets and stores to a new set

# ---------- Difference Operation ----------
set_x = {"cat", "dog", "fish"}
set_y = {"dog", "bird"}
print(set_x.difference(set_y)) # Finds the different items, that are non duplicates between the two sets and stores to a new set

