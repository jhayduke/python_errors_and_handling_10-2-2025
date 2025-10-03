# DRY - DONT REPEAT YOURSELF
# print("Hi, Javian!")
# print("Welcome to class!")

# print("Hi, Joe!")
# print("Welcome to class!")

# print("Hi, Troy!")
# print("Welcome to class!")

def say_hello(name = "No name"):
  print(f"Hi, {name}!")
  print("Welcome to class!")

say_hello("Javian")
say_hello("Edi")
say_hello("Joe")

say_hello()


# user_name = input("Enter your name: ")
# say_hello(user_name)


def area(width = 5, height = 3):
  print(f"The area for {width} and {height} is {width*height}")

area(3,5)

area(9,84)

area()

area(10)

area(height=11)


def introduce(name, age):
  print(f"{name} is {age} years old.")

introduce("Sally", 29)
introduce( 29, "John") #Order matters
introduce( age = 29, name = "John")



message = "I am a global scope"

def show_message():
  # global message
  
  message = "Hello everyone"

  # Access the message variable in the global scope
  print(message)

show_message()

print(message)