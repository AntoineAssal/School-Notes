# Python Language Review
Lines starting with `>>>` represents the standard Python interactive REPL prompt:
```py
$ python      # From a terminal, start the Python interpreter in interactive mode
>>> x = 42    # Create a new variable 'x' and make it refer to an integer object that holds value 42
>>> x         # Print whatever 'x' is, in interactive mode
42
>>> print(x)  # Print whatever 'x' is, even if we weren't in interactive mode
42
>>> quit()    # Quit Python interpreter back to terminal
$ 
```
## Variables
A Python variable is a symbol that refers to an object. Never confuse the symbol (the variable name) with the object that it refers to. They are two different things. If you fail to understand this, you will live in a world of confusion.
```py
>>> x = 5    # Create a new variable 'x' and make it refer to an integer object that holds value 5
>>> y = x    # Create a new variable 'y' and make it refer to the same integer object as 'x'
>>> x += 10  # Make 'x' refer to a new integer object with value (x + 10)
>>> x        # Variable x now refers to the new integer object, with value 15
15
>>> y        # Variable y still refers to the old integer object, with value 5
5
```
Important to keep in mind the difference between the `==` and `is` operators.
```py
>>> x = 257     # Make 'x' refer to an integer object that holds value 257
>>> x == 257    # Does x refer to an object that has SAME VALUE as this other integer object?
True            # Yes!
>>> x is 257    # Does x refer to EXACT SAME OBJECT as this other integer object?
False           # No! There are two different integer objects in memory, each with value 257
```
The result would be different for integers 0..256 because Python tries to save memory by pooling small integers. Likewise for short strings.

## Numbers

Need to know the difference between float division (the default) and integer division:
```py
>>> 3 / 2           # In Python 3, dividing two integers results in a floating-point value
1.5
>>> 3 // 2          # In Python 3, you must use the // operator to force integer division
1
```
as well as the `**` exponentiation operator:
```py
>>> 2**3            # 2 cubed
8
>>> 2**0.5          # square root of 2
1.4142135623730951
```
How to express floating-point numbers (float) in scientific notation:
```py
>>> 1e-3            # Same as 10**(-3), but prefer scientific notation
0.001

>>> 1e3             # A number expressed in scientific notation is always of type float
1000.0
```
Python `floats` are `64-bit`, like a `double` in `C`:
```py
>>> 1e-323 == 0.0   # Very very tiny value
False
>>> 1e-324 == 0.0   # So tiny we can't represent it with 64-bit float anymore, rounds down to 0.0
True
```