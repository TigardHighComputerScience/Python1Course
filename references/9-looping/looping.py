# Range of numbers between 1 and 9
my_range = range(1, 10)

# Note the unusual output of the range object
print(my_range, type(my_range))

# Print all the numbers in the range object
for x in my_range:
    print(x)

# Shorter version of the above loop
for x in range(1, 10):
    print(x)

# Print elements from a list
my_list = [2, "hello", "apple", 3.2]

for x in my_list:
    print(x)

# Using a while loop to print out 1 to 3
my_int = 1

while my_int < 4:
    print(my_int)
    my_int += 1

