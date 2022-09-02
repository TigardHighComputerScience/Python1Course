# Functions

Functions are a core part of any programming language. They allow us
to separate and reuse code.

```python3
def my_function():
    print("Hello World")
```

By itself, this code does nothing. All it does is create an object, containing a code block, that we can call later.

```python3
my_function()
```

```Output
Hello World
```

This function call is extremely basic and more importantly not very useful.
In this example it would make more sense to call print by itself.

This is a more useful example.

```python3
def print_names(names):
    for name in names:
        print("Hello " + name + "! Nice to meet you!")

names = ["John", "Jane", "Bob", "Alice"]

print_names(names)
```

```Output
Hello John! Nice to meet you!
Hello Jane! Nice to meet you!
Hello Bob! Nice to meet you!
Hello Alice! Nice to meet you!
```

The `names` in `my_function(names)` is called a parameter. A local variable to be used inside the function.

This example of a function is more realistic to something you would write yourself, but still very simple. No space was saved, however it did become extremely easy to read and see what was happening.

## `return`

The `return` keyword is used to return a value from a function. A function that reaches a `return` keyword will return the value and exit.

```python3
def add(a, b):
    return a + b

my_int = add(1, 2)

print(my_int)
```

```Output
3
```

<sub>[Take me to the next section]()</sub>
