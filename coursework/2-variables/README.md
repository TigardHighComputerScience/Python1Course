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
```
My int holds the value of:  5
My string holds the value of:  Hello
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

If you are ever wondering what type a variable is you can use the `type` 
function.

```python3
print("My int is of type: ", type(my_int))
print("My string is of type: ", type(my_string))
```
```
My int is of type:  <class 'int'>
My string is of type:  <class 'str'>
```

<sub>[Take me to the next section](https://github.com/TigardHighComputerScience/Python1References/tree/main/coursework/3-user_input)</sub>
