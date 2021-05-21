# Lambda Functions
How to define a function using lambda notation:
```py
>>> f = lambda x: x*x   # Create a function object and make a new variable 'f' that refers to it
>>> f
<function <lambda> at 0x0000023EEC452B88>

>>> f(5)                # Call the function object referred to by variable 'f'
25
```
How to use lambdas as arguments to other functions:
```py
>>> x = [1, -5, -3, 2]
>>> sorted(x)                         # Sort the list by directly comparing pairs x[i] < x[j]
[-5, -3, 1, 2]

>>> sorted(x, key=lambda y: y**2)     # Sort the list by comparing key(x[i]) < key(x[j]), where the 'key'
[1, 2, -3, -5]                        # argument refers to a function object taking one argument
```
Above, we could have used the absolute value `(sorted(x, key=abs))` to achieve the same effect as squaring the key `(y**2)`, even though `abs` is not a lambda function.

