# name = "Allan"

# print(name)

students = ["Joe", "Troy", "Anthony", "Nataysia"]

print(students[1])

print("The first student is ", students[0])

mixed = ["Alice", 25, True, 3.14]

print(mixed)

# Prints the last item in the list
print(mixed[-1])

print(f"The mixed list has {len(mixed)} items")

try:
  print(mixed[6])
except IndexError as e:
  print("Error:", e)


numbers = [1, 2, 3]

# Changing an existing element
numbers[1] = 20

print("After change:", numbers)

# Add to end of list
numbers.append(4)
print("After append:", numbers)

# Insert at specific position
numbers.insert(1, 2)
print("After insert:", numbers)

# Remove the last element
popped_num = numbers.pop()
print("After pop:", numbers)
print(f"The number {popped_num} has been removed successfully")

# Remove specific item
numbers.remove(20)
print("After remove:", numbers)

# Remove by index
numbers.pop(1)
print("after pop(1):", numbers)



movies = ['Inception', 'The Matrix', 'Interstellar', 'Avatar', 'Dune']
random = [4,8,6,2,9]
user_input = []

print(movies[0])
print(movies[-1])

random[2] = 30
movies.append("Barbie")
movies.append("Rush Hour")
print(random)
print("Total number of movies:", len(movies))
movies.pop()

print(movies)


# if(5 in random):
#   print(True)
# else:
#   print(False)

print(f"Is 5 in random: {5 in random}")


# numbers: 0, 1 ,2 ,3 ,4
for number in range(5):
  print(number)


fruits = ["apple", "orange", "Kiwi"]

for fruit in fruits:
  print("The fruit is", fruit)


numbers = [1, 2, 3, 4]

for num in numbers:
  print(f"The square of {num} is {num*num}")