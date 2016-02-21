Exercise description from p.27
=====================

Exercise 3.3. Note: This exercise should be done using only the statements and other features we
have learned so far.

1. Write a function that draws a grid like the following:
```
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
```
Hint: to print more than one value on a line, you can print a comma-separated sequence of
values:

`print('+', '-')`

By default, `print` advances to the next line, but you can override that behavior and put a
space at the end, like this:
```
print('+', '-')
print('-')
```
The output of these statements is `+ -` .

A `print` statement with no argument ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.