# Boolean values, If statements, Logical operators

## Boolean Values

A boolean value, often referred to as a `bool` is a value of either `True` or `False`.

```python3
my_bool = True
print(my_bool)
```

```Output
True
```

## If Statements

If statements are used to execute a block of code based on a certain condition.

```python3
my_bool = True

if my_bool:
    print("Python makes sense")
```

```Output
Python makes sense
```

For more advanced if statement expressions you can use the `else` and the `elif` keyword.

```python3
my_bool = False

if my_bool
    print("Python makes sense")
else:
    print("Our boolean is false :(")
```

```Output
Our boolean is false :(
```

```python3
my_bool = False
another_bool = True

if my_bool:
    print("Python makes sense")
elif another_bool:
    print("Second time is the charm")
else:
    print("All booleans are false :(")
```

```Output
Second time is the charm
```

Notice how the `else` keyword is only executed if all above `if` or `elif` statements are false.

## Logical Operators

Logical Operators are used to make more complex if statements.

```python3
if 1 == 2:
    print("Wait, 1 is equal to 1?")
elif 1 == 1:
    print("1 is equal to 1")
else:
    print("What does 1 equal?")
```

```Output
1 is equal to 1
```

Logical Operators compare the left value to the right value, returning a `True` or a `False`.

Visit the [Logical Operator Reference Table]() for all of the logical operators.

The main feature of logical operators is in if statements such as the one above, however you can also use them to evaluate the value of a `bool`.

```python3
my_bool = 5 <= 6

print(my_bool)
```

```Output
True
```

<sub>[Take me to the next section]()</sub>