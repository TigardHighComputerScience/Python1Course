# String Operators

Objects in python all have operators that can be used on them. A string is a 
basic object in python that we will use as an example.

For example we could concatenate two strings together using the `+` operator.

```python3
my_string = "Hello"
my_other_string = " World"

my_string = my_string + my_other_string
print(my_string)
```

```
Hello World
```

Don't forget about `shorthand assignment`:

```python3
my_string += my_other_string
print(my_string)
```

```
Hello World
```

You can also use these operators in a plain `print` function.

```python3
print("Hello" + " World")
```

```
Hello World
```

If you want to print a string along with a number you can convert the number
to a string using the `str` function. Then you can concatenate them together.

```python3
my_number = 5
my_string = "My number is " + str(my_number)
print(my_string)
```

```
My number is 5
```

Believe it or not, you can also multiply string with the `*` operator.

```python3
my_string = "Hello "
print(my_string * 3)
```

```
Hello Hello Hello
```

<sub>[Take me to the next section](https://github.com/TigardHighComputerScience/Python1Course/tree/main/references/6-comments)</sub>
