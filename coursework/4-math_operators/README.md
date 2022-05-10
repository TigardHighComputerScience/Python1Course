# Math Operators

Math operators or just operators are used to change the value of variables.

For example lets take x and y and add them together.

```python3
x = 5
y = 2

print("The sum of x and y is:", x + y)
```
```
The sum of x and y is: 7
```

This works just like you would expect. You can also take `x + y` and assign it
to a new variable.

```python3
x = 5
y = 2

z = x + y

print("The sum of x and y is:", z)
```
```
The sum of x and y is: 7
```

If you wanted to add the value of `y` to the value of `x` you could do something
like this

```python3
x = 5
y = 2

x = x + y

print("The sum of x and y is:", x)
```
```
The sum of x and y is: 7
```

And just like that the value of `x` is now the value of `x + y` or `7`.

There is another way to do this called `shorthand assignment` using the `+=` 
operator.

```python3
x = 5
y = 2

x += y

print("The sum of x and y is:", x)
```
```
The sum of x and y is: 7
```

This is the preferred way to do this because of two main reasons.
1. It is easier to read.
2. It is faster for the computer to do the calculation.

The computer can preform this shorthand calculation faster because `x` only
needs to be referenced once. In the previous example `x` was referenced twice.

This will save a insignificant amount of time for the computer, as it takes
essentialy no time to access a variable but it is important to mention it none 
the less.

Python, just like any other programmnig language, has loads of math operators 
that each do different things.
1. `+`: Addition
2. `-`: Subtraction
3. `*`: Multiplication
4. `/`: Division
5. `//`: Floor Division
6. `**`: Exponent
7. `%`: Modulus

You will learn what each one does and how to use them as you gain more and
more experience with programming. Check [this](https://github.com/TigardHighComputerScience/Python1References/blob/main/coursework/4-math_operators/operator_reference_table.md) 
reference table for what all of the math operators do.

It's important to note that all of these operators have a 
`shorthand assignment` form.

1. `+=`: Addition and Assignment
2. `-=`: Subtraction and Assignment
3. `*=`: Multiplication and Assignment
4. `/=`: Division and Assignment
5. `//=`: Floor Division and Assignment
6. `**=`: Exponent and Assignment
7. `%=`: Modulus and Assignment

<sub>[Take me to the next section]()</sub>