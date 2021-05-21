# Strings
Different ways to create strings:
```py
>>> s = 'hello'      # Make a new variable 's' and have it refer to a new string object with value 'hello'
>>> s = "hello"      # Same thing
>>> s = """hello"""  # Same thing
>>> s
'hello'              # By default Python displays strings with single quotes around them
>>> print(s)
hello                # Printing a string does not result in surrounding quotes
```
The triple-quote is special because it lets you define multi-line strings, which is useful for documentation:

```py
>>> print('first\nsecond')  # Single quotes require escape character \n (newline)
first
second

>>> print("""first
... second""")              # Triple-quotes let you write multiple lines of text right into the string
first
second
```
We can treat strings like a sequence of characters:
```py
>>> s = 'abcd'
>>> s[2]         # Get the character at index 2 (the third character)
'c'
>>> len(s)       # Get the length of the string (the number of characters)
4
```
We can append strings together:
```py
>>> s = 'before ' + s + ' after'  # Make 's' refer to a new string object built from the old value
>>> s
'before abcd after'
```
We can get a string representation of most Python objects:
```py
>>> x = 123
>>> str(x)
'123'
```
We can also split and join strings together:
```py
>>> words = 'Dog versus cat'.split()     # Split a string by whitespace
>>> words
['Dog', 'versus', 'cat']                 # The result is a list of string objects

>>> '-'.join(words)                      # Make a string object with value '-' and then call its join()
'Dog-versus-cat'                         # method to build a new string from a list of other strings
```
## String Formatting
```py
>>> name = 'Jack'
>>> age = 7
>>> '%s is %d years old' % (name, age)
'Jack is 7 years old'
```
The formatting scheme is similar to the printf function in C, where %s means string, %.2f means "floating point value with 2 decimals of precision," etc.

