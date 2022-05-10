# User Input

Just like printing to console python makes taking user input quick and easy.
To take user input you use the `input` function.

```python3
user_input = input("Enter your name: ")
```

This will store whatever the user enters in the variable `user_input`.

By default the `input` function will convert the input into a string, even
if the user enters a number such as `5`.

To get a user input of a number you will need to convert the output of the
`input` function into a number using the `int` function.

```python3
user_input = int(input("Enter a number: "))
```

Now if you use the `type` function to test the `user_input` variable it will
have a type of `int`. This will work the same for all basic types, such as 
float.

Be careful, if you want a number and the user enters a string you will get
an error message, you will learn how to account for this in the `exceptions` 
section of this course.

<sub>[Take me to the next section](https://github.com/TigardHighComputerScience/Python1References/tree/main/coursework/4-math_operators)</sub>