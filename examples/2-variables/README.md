# Variables and Types

A variable is an object that stores information. For example a `int` or `string`

```python3
my_int = 5
my_string = "Hello"
```

These are called `variables` and they simply hold information that can be 
used later.

```python3
print("My int holds the value of: ", my_int)
print("My string holds the value of: ", my_string)
```

Here is a list of some basic types:
- `int`
- `string`
- `float`

Python has no character type, insted simply refer to it as a `string` with a 
length of `1`.

These basic variables are `mutable` meaning can be changed. If you want to 
indicate that a variable should not be changed mark it all in caps.

```python3
DONT_CHANGE_THIS_INT = 5
```

By default this does not prevent you from changing the variable, only indicating
and reminding you not to.

If you are ever woundering what type a variable is you can use the `type` 
function.

```python3
print("My int is of type: ", type(my_int))
print("My string is of type: ", type(my_string))
```

<sub>[Take me to the next page]()</sub>