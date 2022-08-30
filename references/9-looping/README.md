# Looping

## `range()`

Before you understand looping it is important to know about the range function.

The `range()` function creates a list of numbers between a start and end value, inclusive exclusive. Meaning the start is included where the end value is not.

```python3
# Range of numbers between 1 and 9
my_range = range(1, 10)
```

Range can be thought of as a list, however in reality it is it's own unique object.

```python3
# Range of numbers between 1 and 9
my_range = range(1, 10)

print(type(my_range))
```

```Output
<class 'range'>
```

## `for` loop

Looping is done using the `for` and `in` key

# Range of numbers between 1 and 9
my_range = range(1, 10)

for x in my_range:
    print(x)
```

```Output
1
2
3
4
5
6
7
8
9
```

- `x` is a temporary variable that is used to store the value of each number in the range.

This example could have been shortened by not saving the range as a separate variable.

```python3
# Print a range of numbers between 1 and 3
for x in range(1, 4):
    print(x)
```

```Output
1
2
3
```

The `for` loop can also be used to loop through a list.

```python3
my_list = [2, "hello", "apple", 3.2]

for x in my_list:
    print(x)
```

```Output
2
hello
apple
3.2
```

## `while` loop

The `while` loop will continue to loop a code block until a condition is no longer met.

```python3
my_int = 1

while my_int < 4:
    print(my_int)
    my_int += 1
```

```Output
1
2
3
```

<sub>[Take me to the next section]()</sub>