# Take user input of a string
user_input = input("Enter a string: ")
print("The user input is: ", user_input)
print("The type of the user input is: ", type(user_input))

# Notice how the type is a string even though we never converted it to one.

# Take user input of a number
# Don't forget to convert the string to a number using `int`
user_input = int(input("Enter a number: "))
print("The user input is: ", user_input)
print("The type of the user input is: ", type(user_input))

# Take user input of a float
# Don't forget to convert the string to a float using `float`
user_input = float(input("Enter a float: "))
print("The user input is: ", user_input)
print("The type of the user input is: ", type(user_input))