# Floating Point Numbers

A floating point number, or float, is a decimal number.

```python3
my_float = 1.2
print(type(my_float))
```

```Output
<class 'float'>
```

Just like other basic data types you can convert to and away from them using the `float()` function.

```python3
my_int = 1
my_float = float(my_int)

print(my_float)
print(type(my_float))
```

```Output
1.0
<class 'float'>
```

Notice how a decimal was added even though it was never used.

You can also convert in the opposite direction.

```python3
my_float = 1.2
my_int = int(my_float)

print(my_int)
print(type(my_int))
```

```Output
1
<class 'int'>
```

When converting away from a float the decimal precision is always lost.

Here are some other uses of a float.

```python3
# Non-floor division
my_float = 7 / 6
print(my_float)

# String to float
my_float = float("1.2")
print(my_float)

# Float to string
my_float = 1.4
my_string = str(my_float)
print(my_string)
```

```Output
1.1666666666666667
1.2
1.4
```

<sub>[Take me to the next section](https://github.com/TigardHighComputerScience/Python1Course/tree/main/references/9-looping)</sub>
