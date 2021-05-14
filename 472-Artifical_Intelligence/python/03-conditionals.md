# Conditionals
We can write if-statements using conditional expressions (`==`, `!=`, `<`, `>`, etc) and also in "word" expressions that are unique to Python like (`in`, `is`):
```py
>>> x = {1, 2}
>>> if 3 in x:
...     print("yep!")
... else:
        print("nope")
nope
```
We can combine or modify conditional expressions with logical operators (`and`, `or`, `not`):
```py
(3 not in x) and (len(x) == 2)
True
```
```py
if 3 in x:
...     print("yep!")
... elif len(x) == 10:
...     print("this?")
... else:
...     print("nope")
nope
```
We can also use a special `if-else` expression, similar to Java's `condition ? yes_value : no_value` python uses the structure `yes_value if condition else no_value`:
```py
>>> y = 'yep!' if 2 in x else 'nope'   # Since integer 2 is in x, return the expression BEFORE the if
>>> y
'yep!'

>>> y = 'yep!' if 3 in x else 'nope'   #
>>> y
'nope'
```